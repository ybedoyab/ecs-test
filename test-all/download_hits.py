"""
Descarga todos los docId de hits.json y genera un PDF por documento en hits/<docId>.pdf

Requiere curl_comando.txt vigente (misma sesión que usaste para el probe).

Uso:
  python download_hits.py
  python download_hits.py --hits-file hits.json --max-pages 100
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import ssl
import sys
import threading
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_PARENT = os.path.normpath(os.path.join(_SCRIPT_DIR, ".."))
if _PARENT not in sys.path:
    sys.path.insert(0, _PARENT)
if _SCRIPT_DIR not in sys.path:
    sys.path.insert(0, _SCRIPT_DIR)

from api_downloader import parse_curl_to_request  # noqa: E402
from probe_docids import replace_doc_id  # noqa: E402

from PIL import Image  # noqa: E402

MIN_PNG_BYTES = 1000
DEFAULT_MAX_PAGES = 250
DEFAULT_WORKERS = 10


def safe_filename(doc_id: str) -> str:
    bad = '<>:"/\\|?*'
    out = "".join(c if c not in bad and ord(c) >= 32 else "_" for c in doc_id)
    return out.strip() or "document"


def replace_total_page(raw_data: str | None, total: int) -> str | None:
    if not raw_data:
        return raw_data
    return re.sub(r'"totalPage"\s*:\s*\d+', f'"totalPage":{total}', raw_data, count=1)


def load_hits(path: str) -> list[str]:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    ids = data.get("docIds") or data.get("doc_ids") or []
    if not isinstance(ids, list):
        print("[!] hits.json: docIds debe ser una lista")
        sys.exit(1)
    return [str(x).strip() for x in ids if str(x).strip()]


def consecutive_slides_from_one(work_dir: str) -> list[str]:
    """slide_001.png, slide_002.png, ... hasta el primer hueco o fin."""
    paths: list[str] = []
    n = 1
    while True:
        name = f"slide_{n:03d}.png"
        p = os.path.join(work_dir, name)
        if not os.path.isfile(p) or os.path.getsize(p) < MIN_PNG_BYTES:
            break
        paths.append(p)
        n += 1
    return paths


def download_all_pages(
    url: str,
    headers: dict,
    raw_data_template: str | None,
    method: str,
    work_dir: str,
    total_pages: int,
    ctx: ssl.SSLContext,
    timeout: float,
    workers: int,
) -> None:
    os.makedirs(work_dir, exist_ok=True)
    lock = threading.Lock()
    count = [0]

    def one_page(page: int) -> None:
        fname = os.path.join(work_dir, f"slide_{page:03d}.png")
        if os.path.isfile(fname) and os.path.getsize(fname) >= MIN_PNG_BYTES:
            with lock:
                count[0] += 1
                print(f"  [{count[0]}/{total_pages}] p.{page} ya existe", end="\r")
            return

        payload_bytes = None
        if raw_data_template:
            payload = re.sub(
                r'("pageNum"\s*:\s*)\d+',
                lambda m: f"{m.group(1)}{page}",
                raw_data_template,
            )
            payload_bytes = payload.encode("utf-8")
        req = urllib.request.Request(url, data=payload_bytes, headers=headers, method=method)

        for intento in range(1, 4):
            try:
                with urllib.request.urlopen(req, context=ctx, timeout=timeout) as response:
                    content = response.read()
                with open(fname, "wb") as f:
                    f.write(content)
                if os.path.getsize(fname) < MIN_PNG_BYTES:
                    try:
                        os.remove(fname)
                    except OSError:
                        pass
                    return
                with lock:
                    count[0] += 1
                    print(f"  [{count[0]}/{total_pages}] p.{page} OK        ", end="\r")
                return
            except Exception as e:
                if intento == 3:
                    with lock:
                        print(f"\n  [!] p.{page}: {e}")
                time.sleep(1)

    with ThreadPoolExecutor(max_workers=workers) as ex:
        ex.map(one_page, range(1, total_pages + 1))


def pngs_to_pdf(image_paths: list[str], pdf_path: str) -> None:
    if not image_paths:
        return
    first = Image.open(image_paths[0]).convert("RGB")
    rest = [Image.open(p).convert("RGB") for p in image_paths[1:]]
    try:
        first.save(pdf_path, save_all=True, append_images=rest)
    finally:
        first.close()
        for im in rest:
            im.close()


def process_one_doc(
    doc_id: str,
    url0: str,
    headers0: dict,
    data0: str | None,
    method: str,
    out_dir: str,
    max_pages: int,
    ctx: ssl.SSLContext,
    timeout: float,
    workers: int,
    skip_existing: bool,
) -> bool:
    safe = safe_filename(doc_id)
    pdf_path = os.path.join(out_dir, f"{safe}.pdf")
    if skip_existing and os.path.isfile(pdf_path) and os.path.getsize(pdf_path) > 100:
        print(f"[*] Saltando (ya existe): {pdf_path}")
        return True

    work_dir = os.path.join(out_dir, "_tmp", safe)
    if os.path.isdir(work_dir):
        shutil.rmtree(work_dir, ignore_errors=True)
    os.makedirs(work_dir, exist_ok=True)

    u, h, d = replace_doc_id(url0, headers0, data0, doc_id)
    d = replace_total_page(d, max_pages)

    print(f"\n[*] DocId {doc_id}  →  hasta {max_pages} páginas (temp: {work_dir})")
    download_all_pages(u, h, d, method, work_dir, max_pages, ctx, timeout, workers)

    slides = consecutive_slides_from_one(work_dir)
    if not slides:
        print(f"[!] Sin páginas válidas para {doc_id}")
        shutil.rmtree(work_dir, ignore_errors=True)
        return False

    print(f"\n[*] PDF: {len(slides)} páginas consecutivas → {pdf_path}")
    pngs_to_pdf(slides, pdf_path)
    shutil.rmtree(work_dir, ignore_errors=True)
    return True


def main() -> None:
    ap = argparse.ArgumentParser(description="Descargar hits.json a PDFs en hits/")
    ap.add_argument(
        "--hits-file",
        default=os.path.join(_SCRIPT_DIR, "hits.json"),
        help="JSON con { \"docIds\": [ ... ] }",
    )
    ap.add_argument(
        "--curl-file",
        default=os.path.join(_PARENT, "curl_comando.txt"),
        help="cURL base (sesión)",
    )
    ap.add_argument(
        "--out-dir",
        default=os.path.join(_SCRIPT_DIR, "hits"),
        help="Carpeta de salida (PDFs como <docId>.pdf)",
    )
    ap.add_argument(
        "--max-pages",
        type=int,
        default=DEFAULT_MAX_PAGES,
        help=f"Tope de páginas a pedir (totalPage en JSON). Por defecto {DEFAULT_MAX_PAGES}",
    )
    ap.add_argument("--workers", type=int, default=DEFAULT_WORKERS)
    ap.add_argument("--timeout", type=float, default=30.0)
    ap.add_argument(
        "--skip-existing",
        action="store_true",
        help="No regenerar PDF si ya existe",
    )
    args = ap.parse_args()

    if not os.path.isfile(args.hits_file):
        print(f"[!] No existe {args.hits_file}")
        sys.exit(1)
    if not os.path.isfile(args.curl_file):
        print(f"[!] No existe {args.curl_file}")
        sys.exit(1)

    doc_ids = load_hits(args.hits_file)
    if not doc_ids:
        print("[!] hits.json no contiene docIds")
        sys.exit(1)

    with open(args.curl_file, encoding="utf-8") as f:
        raw = f.read()
    if "curl" not in raw.lower():
        print("[!] curl_comando.txt no parece un cURL")
        sys.exit(1)

    url0, headers0, data0, method = parse_curl_to_request(raw)
    if not url0:
        print("[!] No se pudo parsear la URL")
        sys.exit(1)

    os.makedirs(args.out_dir, exist_ok=True)

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    ok = 0
    for doc_id in doc_ids:
        if process_one_doc(
            doc_id,
            url0,
            headers0,
            data0,
            method,
            args.out_dir,
            args.max_pages,
            ctx,
            args.timeout,
            args.workers,
            args.skip_existing,
        ):
            ok += 1

    # limpiar _tmp vacío
    tmp_root = os.path.join(args.out_dir, "_tmp")
    if os.path.isdir(tmp_root) and not os.listdir(tmp_root):
        try:
            os.rmdir(tmp_root)
        except OSError:
            pass

    print(f"\n[*] Listo: {ok}/{len(doc_ids)} documentos con PDF en {args.out_dir}")


if __name__ == "__main__":
    main()
