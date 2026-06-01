import os
import re
import ssl
import sys
import threading
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from PIL import Image


def _clean_caret(text):
    text = re.sub(r"\^[\r\n]+", "", text)
    return re.sub(r"\^([\s\S])", r"\1", text)


def _parse_curl(curl_str):
    clean = _clean_caret(curl_str)
    url_match = re.search(r"(https?://[^\s\"\'\^]+)", clean)
    url = url_match.group(1).strip().strip('"').strip("'") if url_match else None
    headers = {}
    for match in re.finditer(r'-H\s+["\']([^:]+):\s*(.*?)["\']', clean):
        headers[match.group(1).strip()] = match.group(2).strip()
    cookie_match = re.search(r'-b\s+["\'](.*?)["\']', clean)
    if cookie_match:
        headers["Cookie"] = cookie_match.group(1)
    data = None
    json_match = re.search(r"(\{.*\})", clean, re.DOTALL)
    if json_match:
        data = json_match.group(1).strip().replace('\\"', '"')
    method = "POST" if data else "GET"
    method_match = re.search(r'-X\s+["\']?([A-Z]+)["\']?', clean)
    if method_match:
        method = method_match.group(1)
    return url, headers, data, method


def run(curl_text, slides_dir: Path, output_pdf: Path):
    url, headers, raw_data, method = _parse_curl(curl_text)
    if not url:
        raise RuntimeError("No se detecto URL en curl_comando.txt")

    total = 1
    if raw_data:
        m = re.search(r'"totalPage"\s*:\s*(\d+)', raw_data)
        if m:
            total = int(m.group(1))

    slides_dir.mkdir(parents=True, exist_ok=True)
    output_pdf.parent.mkdir(parents=True, exist_ok=True)

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    lock = threading.Lock()
    done = [0]

    def fetch_page(page):
        path = slides_dir / f"slide_{page:03d}.png"
        if path.exists() and path.stat().st_size > 1000:
            with lock:
                done[0] += 1
                print(f"  [{done[0]}/{total}] slide {page} ok", end="\r")
            return
        payload = None
        if raw_data:
            payload = re.sub(
                r'("pageNum"\s*:\s*)\d+',
                lambda m: f"{m.group(1)}{page}",
                raw_data,
            ).encode("utf-8")
        req = urllib.request.Request(url, data=payload, headers=headers, method=method)
        for attempt in range(3):
            try:
                with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
                    data = resp.read()
                path.write_bytes(data)
                if path.stat().st_size < 1000:
                    path.unlink(missing_ok=True)
                    return
                with lock:
                    done[0] += 1
                    print(f"  [{done[0]}/{total}] slide {page} ok", end="\r")
                return
            except Exception as e:
                if attempt == 2:
                    print(f"\nError pagina {page}: {e}", file=sys.stderr)
                time.sleep(1)

    print(f"Descargando {total} diapositivas...")
    with ThreadPoolExecutor(max_workers=10) as ex:
        ex.map(fetch_page, range(1, total + 1))
    print()

    files = sorted(slides_dir.glob("slide_*.png"))
    if not files:
        raise RuntimeError("No se descargaron imagenes")

    images = [Image.open(f).convert("RGB") for f in files]
    images[0].save(
        output_pdf,
        save_all=True,
        append_images=images[1:],
    )
    for f in files:
        f.unlink(missing_ok=True)
    print(f"PDF: {output_pdf}")
