import io
import queue
import threading
import time
from pathlib import Path

import fitz
import numpy as np
from PIL import Image

WORKERS = 4
BUFFER = 15
JPEG_QUALITY = 75
MAX_WIDTH = 1280


def _load_reader():
    import easyocr
    return easyocr.Reader(["es", "en"], gpu=False)


def run(input_pdf: Path, output_pdf: Path):
    if output_pdf.exists():
        print(f"OCR ya existe: {output_pdf}")
        return
    if not input_pdf.exists():
        raise FileNotFoundError(input_pdf)

    print("Cargando EasyOCR...")
    reader = _load_reader()
    doc = fitz.open(input_pdf)
    total = len(doc)
    task_q = queue.Queue(maxsize=BUFFER)
    ocr_results = {}
    render_data = {}
    lock = threading.Lock()
    done = [0]

    def worker():
        while True:
            item = task_q.get()
            if item is None:
                task_q.task_done()
                break
            idx, img_np = item
            try:
                ocr_results[idx] = reader.readtext(img_np)
            except Exception:
                ocr_results[idx] = []
            with lock:
                done[0] += 1
                print(f"  OCR [{done[0]}/{total}]", end="\r")
            task_q.task_done()

    threads = [threading.Thread(target=worker, daemon=True) for _ in range(WORKERS)]
    for t in threads:
        t.start()

    for i in range(total):
        page = doc[i]
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
        if pix.n >= 4:
            img = Image.frombytes("RGBA", [pix.width, pix.height], pix.samples)
            bg = Image.new("RGB", img.size, (255, 255, 255))
            bg.paste(img, mask=img.split()[3])
            img = bg
        else:
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        if img.width > MAX_WIDTH:
            ratio = MAX_WIDTH / float(img.width)
            img = img.resize((MAX_WIDTH, int(img.height * ratio)), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=JPEG_QUALITY, optimize=True)
        render_data[i] = {
            "jpeg": buf.getvalue(),
            "w": page.rect.width,
            "h": page.rect.height,
            "ow": img.width,
            "oh": img.height,
        }
        task_q.put((i, np.array(img)))

    doc.close()
    task_q.join()
    for _ in threads:
        task_q.put(None)
    for t in threads:
        t.join()

    out = fitz.open()
    for i in range(total):
        d = render_data[i]
        page = out.new_page(width=d["w"], height=d["h"])
        page.insert_image(page.rect, stream=d["jpeg"])
        sx = d["w"] / max(d["ow"], 1)
        sy = d["h"] / max(d["oh"], 1)
        for bbox, text, prob in ocr_results.get(i, []):
            if prob < 0.2:
                continue
            x0 = float(bbox[0][0]) * sx
            y0 = float(bbox[0][1]) * sy
            x1 = float(bbox[2][0]) * sx
            y1 = float(bbox[2][1]) * sy
            try:
                page.insert_text(
                    fitz.Point(x0, y1),
                    text,
                    fontname="helv",
                    fontsize=fitz.Rect(x0, y0, x1, y1).height * 0.9,
                    render_mode=3,
                )
            except Exception:
                pass

    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    out.save(output_pdf, garbage=4, deflate=True, clean=True)
    out.close()
    print(f"\nOCR: {output_pdf}")
