import io
import os
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import fitz
from PIL import Image

JPEG_QUALITY = 75
MAX_WIDTH = 1280


def _compress_image(item):
    xref, width, height, samples, n = item
    try:
        if n == 4:
            img = Image.frombytes("RGBA", [width, height], samples).convert("RGB")
        elif n == 3:
            img = Image.frombytes("RGB", [width, height], samples)
        else:
            pix = fitz.Pixmap(fitz.csRGB, fitz.Pixmap(fitz.csRGB, width, height, samples, 0))
            img = Image.frombytes("RGB", [width, height], pix.samples)
        if img.width > MAX_WIDTH:
            ratio = MAX_WIDTH / float(img.width)
            img = img.resize((MAX_WIDTH, int(img.height * ratio)), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=JPEG_QUALITY, optimize=True)
        return xref, buf.getvalue()
    except Exception:
        return xref, None


def _optimize_doc(doc):
    seen = set()
    batch = []
    xref_page = {}
    for i in range(len(doc)):
        for img in doc[i].get_images():
            xref = img[0]
            if xref in seen:
                continue
            seen.add(xref)
            xref_page[xref] = i
            try:
                pix = fitz.Pixmap(doc, xref)
                batch.append((xref, pix.width, pix.height, pix.samples, pix.n))
            except Exception:
                pass
    if not batch:
        return
    for xref, data in ThreadPoolExecutor().map(_compress_image, batch):
        if not data:
            continue
        page = doc[xref_page[xref]]
        if hasattr(page, "replace_image"):
            page.replace_image(xref, stream=data)
        elif hasattr(doc, "replace_image"):
            doc.replace_image(xref, stream=data)
        else:
            doc.update_stream(xref, data)


def run(input_pdf: Path, output_pdf: Path):
    if not input_pdf.exists():
        raise FileNotFoundError(input_pdf)
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(input_pdf)
    before = os.path.getsize(input_pdf)
    _optimize_doc(doc)
    doc.save(output_pdf, garbage=4, deflate=True, clean=True)
    doc.close()
    after = os.path.getsize(output_pdf)
    pct = (1 - after / before) * 100 if before else 0
    print(f"Comprimido: {output_pdf} ({pct:.0f}% menos)")
