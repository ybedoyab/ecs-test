"""
Prueba múltiples docId reutilizando un solo comando cURL (cookies + EDM-Authorization).
No sustituye la sesión: si caduca, vuelve a pegar un cURL fresco en curl_comando.txt.

Sin argumentos: usa candidatos.txt si existe; si no, barrido M1T9A107N+19d con ≥100 candidatos y, si el log
deja menos de 100 por probar, amplía la ventana automáticamente. Log: probe_tried.jsonl.

Uso:
  python probe_docids.py
  python probe_docids.py --list ids.txt
  python probe_docids.py --ids ID1,ID2,ID3
  python probe_docids.py --numeric-prefix M1T9A107N --from 1234521824182096020 --to 1234521824182096050
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import ssl
import sys
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

# Importar parser del script padre
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_PARENT = os.path.normpath(os.path.join(_SCRIPT_DIR, ".."))
if _PARENT not in sys.path:
    sys.path.insert(0, _PARENT)

from api_downloader import parse_curl_to_request  # noqa: E402

DEFAULT_LIST_FILE = "candidatos.txt"
DEFAULT_LOG_FILE = "probe_tried.jsonl"
DEFAULT_DELAY = 0.35
DEFAULT_WORKERS = 6
DEFAULT_WINDOW = 40

# En modo patrón (sin candidatos.txt / sin --ids): al menos tantos candidatos y, si el log los saltó,
# ampliar ventana hasta tener al menos MIN_PROBE_PER_RUN ids nuevos por corrida (tope MAX_PATTERN_WINDOW).
MIN_PROBE_PER_RUN = 100
MAX_PATTERN_WINDOW = 500_000
PATTERN_EXPAND_STEP = 40

# Patrón por defecto (Huawei EDM / previewer)
DEFAULT_DOC_PREFIX = "M1T9A107N"
DEFAULT_SUFFIX_WIDTH = 19
# Si el docId del cURL no sigue el patrón, se usa este sufijo como centro del barrido
DEFAULT_PATTERN_CENTER_SUFFIX = 1234521824182096028


def min_window_for_min_ids(n: int) -> int:
    """Ventana mínima con 2*w+1 >= n (n candidatos en el barrido simétrico)."""
    if n <= 1:
        return 0
    return math.ceil((n - 1) / 2)


def dedupe_preserve(ids: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for d in ids:
        if d not in seen:
            seen.add(d)
            out.append(d)
    return out


def is_default_pattern_scan(args) -> bool:
    if args.ids or args.list or args.numeric_prefix:
        return False
    default_list = os.path.join(_SCRIPT_DIR, DEFAULT_LIST_FILE)
    return not os.path.isfile(default_list)


class RateLimiter:
    """Espaciado mínimo entre inicios de petición (global, entre hilos)."""

    def __init__(self, min_interval: float):
        self.min_interval = max(0.0, min_interval)
        self._lock = threading.Lock()
        self._last = 0.0

    def wait(self) -> None:
        if self.min_interval <= 0:
            return
        with self._lock:
            now = time.monotonic()
            wait_s = self._last + self.min_interval - now
            if wait_s > 0:
                time.sleep(wait_s)
            self._last = time.monotonic()


def replace_doc_id(url: str, headers: dict, raw_data: str | None, new_doc_id: str) -> tuple[str, dict, str | None]:
    if not url:
        return url, headers, raw_data
    new_url = re.sub(r"/documents/[^/?]+", f"/documents/{new_doc_id}", url, count=1)
    new_headers = dict(headers)
    if "Referer" in new_headers:
        new_headers["Referer"] = re.sub(
            r"([?&]docId=)[^&]*",
            rf"\g<1>{new_doc_id}",
            new_headers["Referer"],
            count=1,
        )
    new_data = raw_data
    if raw_data:
        new_data = re.sub(
            r'"docId"\s*:\s*"[^"]*"',
            f'"docId":"{new_doc_id}"',
            raw_data,
            count=1,
        )
    return new_url, new_headers, new_data


def probe_one(
    url: str,
    headers: dict,
    raw_data_template: str | None,
    method: str,
    ctx: ssl.SSLContext,
    timeout: float,
) -> tuple[bool, int, str | None, bytes | None]:
    """Una sola petición (página 1). Devuelve (éxito, tamaño, content-type o error, cuerpo si éxito)."""
    payload_bytes = None
    if raw_data_template:
        payload = re.sub(
            r'("pageNum"\s*:\s*)\d+',
            lambda m: f"{m.group(1)}1",
            raw_data_template,
            count=1,
        )
        payload_bytes = payload.encode("utf-8")
    req = urllib.request.Request(url, data=payload_bytes, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=timeout) as resp:
            body = resp.read()
            ctype = resp.headers.get("Content-Type", "")
    except urllib.error.HTTPError as e:
        return False, 0, str(e.code), None
    except Exception as e:
        return False, 0, str(e), None

    n = len(body)
    ok = n >= 1000 and ("image" in ctype.lower() or body[:8] == b"\x89PNG\r\n\x1a\n")
    return ok, n, ctype or None, body if ok else None


def load_curl(path: str) -> str:
    if not os.path.isfile(path):
        print(f"[!] No existe: {path}")
        sys.exit(1)
    with open(path, encoding="utf-8") as f:
        return f.read()


def read_id_file(path: str) -> list[str]:
    ids: list[str] = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                ids.append(line)
    return ids


def load_tried_doc_ids(log_path: str) -> set[str]:
    tried: set[str] = set()
    if not os.path.isfile(log_path):
        return tried
    with open(log_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                o = json.loads(line)
                if isinstance(o, dict) and "docId" in o:
                    tried.add(str(o["docId"]))
            except json.JSONDecodeError:
                tried.add(line)
    return tried


def append_log_line(log_path: str, record: dict, log_lock: threading.Lock) -> None:
    line = json.dumps(record, ensure_ascii=False) + "\n"
    with log_lock:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(line)


def default_ids_pattern(base_doc_id: str | None, window: int) -> list[str]:
    """
    Barrido M1T9A107N + sufijo numérico con ancho fijo 19 (ceros a la izquierda).
    Centro: docId del cURL si cumple el patrón; si no, DEFAULT_PATTERN_CENTER_SUFFIX.
    """
    prefix = DEFAULT_DOC_PREFIX
    w = DEFAULT_SUFFIX_WIDTH
    n: int | None = None
    if base_doc_id:
        m = re.fullmatch(rf"{re.escape(prefix)}(\d+)", base_doc_id)
        if m:
            n = int(m.group(1))
    if n is None:
        n = DEFAULT_PATTERN_CENTER_SUFFIX
    lo = max(0, n - window)
    hi = n + window
    return [f"{prefix}{str(i).zfill(w)}" for i in range(lo, hi + 1)]


def iter_doc_ids_explicit(args) -> list[str]:
    ids: list[str] = []
    if args.ids:
        ids.extend(x.strip() for x in args.ids.split(",") if x.strip())
    if args.list:
        ids.extend(read_id_file(args.list))
    if args.numeric_prefix:
        if args.nfrom is None or args.nto is None:
            print("[!] Con --numeric-prefix hacen falta --from y --to")
            sys.exit(1)
        if args.nfrom > args.nto:
            print("[!] --from debe ser <= --to")
            sys.exit(1)
        w = args.width
        for n in range(args.nfrom, args.nto + 1):
            suffix = str(n).zfill(w) if w else str(n)
            ids.append(f"{args.numeric_prefix}{suffix}")
    return ids


def resolve_doc_ids(args, base_doc_id: str | None) -> list[str]:
    ids = iter_doc_ids_explicit(args)
    if ids:
        return ids
    default_list = os.path.join(_SCRIPT_DIR, DEFAULT_LIST_FILE)
    if os.path.isfile(default_list):
        print(f"[*] Usando lista por defecto: {default_list}")
        return read_id_file(default_list)
    win = max(args.window, min_window_for_min_ids(MIN_PROBE_PER_RUN))
    ids = default_ids_pattern(base_doc_id, win)
    center = base_doc_id if base_doc_id and re.fullmatch(
        rf"{re.escape(DEFAULT_DOC_PREFIX)}\d+", base_doc_id
    ) else f"{DEFAULT_DOC_PREFIX}{str(DEFAULT_PATTERN_CENTER_SUFFIX).zfill(DEFAULT_SUFFIX_WIDTH)}"
    print(
        f"[*] Sin candidatos.txt: patrón {DEFAULT_DOC_PREFIX}+"
        f"{DEFAULT_SUFFIX_WIDTH}d, ±{win} alrededor de {center} ({len(ids)} ids, mín. {MIN_PROBE_PER_RUN})"
    )
    return ids


def main() -> None:
    ap = argparse.ArgumentParser(description="Probar docId contra el previewer (mismo cURL base).")
    ap.add_argument(
        "--curl-file",
        default=os.path.join(_PARENT, "curl_comando.txt"),
        help="Ruta al curl_comando.txt con sesión válida",
    )
    ap.add_argument(
        "--delay",
        type=float,
        default=DEFAULT_DELAY,
        help=f"Segundos mínimos entre inicios de petición (global). Por defecto {DEFAULT_DELAY}",
    )
    ap.add_argument(
        "--workers",
        type=int,
        default=DEFAULT_WORKERS,
        help=f"Hilos concurrentes. Por defecto {DEFAULT_WORKERS}",
    )
    ap.add_argument("--timeout", type=float, default=30.0)
    ap.add_argument("--save-dir", default="", help="Si se indica, guarda la página 1 de cada acierto como PNG")
    ap.add_argument("--ids", default="", help="Lista separada por comas de docId")
    ap.add_argument("--list", default="", help="Archivo con un docId por línea (# comentarios)")
    ap.add_argument(
        "--numeric-prefix",
        default="",
        help=f"Prefijo para --from/--to (por defecto sin args se usa {DEFAULT_DOC_PREFIX}+{DEFAULT_SUFFIX_WIDTH}d)",
    )
    ap.add_argument("--from", dest="nfrom", type=int, default=None)
    ap.add_argument("--to", dest="nto", type=int, default=None)
    ap.add_argument("--width", type=int, default=0, help="Ancho con ceros a la izquierda para el sufijo numérico")
    ap.add_argument(
        "--window",
        type=int,
        default=DEFAULT_WINDOW,
        help=(
            f"Sin candidatos.txt: radio base del barrido ({DEFAULT_DOC_PREFIX}+{DEFAULT_SUFFIX_WIDTH}d). "
            f"Por defecto {DEFAULT_WINDOW}; se usa al menos ±{min_window_for_min_ids(MIN_PROBE_PER_RUN)} "
            f"para ≥{MIN_PROBE_PER_RUN} candidatos y se amplía si el log deja <{MIN_PROBE_PER_RUN} por ejecutar."
        ),
    )
    ap.add_argument(
        "--log-file",
        default=os.path.join(_SCRIPT_DIR, DEFAULT_LOG_FILE),
        help=f"JSONL de intentos (se reutiliza para saltar). Por defecto {DEFAULT_LOG_FILE} en esta carpeta",
    )
    ap.add_argument(
        "--no-skip-log",
        action="store_true",
        help="No saltar ids que ya aparezcan en el log (sigue appendiendo al log)",
    )
    args = ap.parse_args()

    raw = load_curl(args.curl_file)
    if "curl" not in raw.lower():
        print("[!] El archivo no parece contener un cURL")
        sys.exit(1)

    url0, headers0, data0, method = parse_curl_to_request(raw)
    if not url0:
        print("[!] No se pudo parsear la URL del cURL")
        sys.exit(1)

    m = re.search(r"/documents/([^/?]+)", url0)
    base_doc_id = m.group(1) if m else None

    default_pattern = is_default_pattern_scan(args)
    doc_ids = resolve_doc_ids(args, base_doc_id)
    doc_ids = dedupe_preserve(doc_ids)

    tried = set() if args.no_skip_log else load_tried_doc_ids(args.log_file)
    to_run = [d for d in doc_ids if d not in tried]

    if default_pattern and not args.no_skip_log:
        w = max(args.window, min_window_for_min_ids(MIN_PROBE_PER_RUN))
        while len(to_run) < MIN_PROBE_PER_RUN and w < MAX_PATTERN_WINDOW:
            w += PATTERN_EXPAND_STEP
            doc_ids = dedupe_preserve(default_ids_pattern(base_doc_id, w))
            to_run = [d for d in doc_ids if d not in tried]
            print(
                f"[*] Ampliando barrido a ±{w} para acercarse a {MIN_PROBE_PER_RUN} ids sin probar "
                f"(ahora {len(to_run)} nuevos, {len(doc_ids)} candidatos)"
            )
        if len(to_run) < MIN_PROBE_PER_RUN:
            print(
                f"[!] Con ventana hasta ±{w} solo hay {len(to_run)} ids fuera del log "
                f"(objetivo {MIN_PROBE_PER_RUN}; tope ±{MAX_PATTERN_WINDOW})."
            )

    skipped = len(doc_ids) - len(to_run)

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    save_dir = args.save_dir.strip()
    if save_dir:
        os.makedirs(save_dir, exist_ok=True)

    limiter = RateLimiter(args.delay)
    log_lock = threading.Lock()
    print_lock = threading.Lock()
    workers = max(1, args.workers)

    print(f"[*] Base URL: {url0[:80]}...")
    print(f"[*] docId en cURL: {base_doc_id}")
    print(f"[*] Log: {args.log_file}  (saltados ya probados: {skipped})")
    print(f"[*] Workers: {workers}  delay entre inicios: {args.delay}s")
    print(f"[*] A probar ahora: {len(to_run)} / {len(doc_ids)} totales\n")

    hits: list[str] = []
    hits_lock = threading.Lock()

    def work(did: str) -> None:
        limiter.wait()
        u, h, d = replace_doc_id(url0, headers0, data0, did)
        ok, size, info, body = probe_one(u, h, d, method, ctx, args.timeout)
        append_log_line(
            args.log_file,
            {
                "docId": did,
                "ok": ok,
                "bytes": size,
                "info": info or "",
                "ts": time.time(),
            },
            log_lock,
        )
        with print_lock:
            if ok:
                print(f"  [OK] {did}  ({size} bytes, {info})")
                with hits_lock:
                    hits.append(did)
                if save_dir and body:
                    path = os.path.join(save_dir, f"hit_{did}_page1.png")
                    try:
                        with open(path, "wb") as out:
                            out.write(body)
                        print(f"       guardado: {path}")
                    except OSError as e:
                        print(f"       [!] no se pudo guardar: {e}")
            else:
                print(f"  [--] {did}  ({info or 'fail'}, {size} B)")

    if not to_run:
        print("[*] Nada que probar (todo estaba ya en el log o lista vacía).")
    else:
        with ThreadPoolExecutor(max_workers=workers) as ex:
            futures = [ex.submit(work, did) for did in to_run]
            for _ in as_completed(futures):
                pass

    print(f"\n[*] Resumen esta ejecución: {len(hits)} acierto(s) de {len(to_run)} probados")
    if hits:
        out_json = os.path.join(_SCRIPT_DIR, "hits.json")
        with open(out_json, "w", encoding="utf-8") as f:
            json.dump({"docIds": hits, "count": len(hits)}, f, indent=2)
        print(f"[*] Aciertos de esta corrida en: {out_json}")


if __name__ == "__main__":
    main()
