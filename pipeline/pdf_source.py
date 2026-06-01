from pathlib import Path

from config import OUTPUT_DIR, ROOT


def resolve_pdf(name: str) -> Path | None:
    n = (name or "lab").strip() or "lab"
    candidates = [
        OUTPUT_DIR / f"{n}_small.pdf",
        OUTPUT_DIR / f"{n}_ocr.pdf",
        OUTPUT_DIR / f"{n}.pdf",
        ROOT / f"Regional_2526_Lab_ocr.pdf",
        ROOT / f"{n}_ocr.pdf",
        ROOT / f"{n}.pdf",
        ROOT / f"{n}_Lab_ocr.pdf",
    ]
    seen = set()
    for p in candidates:
        key = str(p).lower()
        if key in seen:
            continue
        seen.add(key)
        if p.is_file():
            return p
    return None
