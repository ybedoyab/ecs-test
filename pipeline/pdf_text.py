import re
from pathlib import Path

import fitz

from config import OUTPUT_DIR

# Cortes del PDF Regional (saltar indice; usar bloque de examen real).
_SECTION_BOUNDS = {
    "openeuler": ("3.1.5 Exam Tasks", "3.2.4 Exam Tasks"),
    "opengauss": ("3.2.4 Exam Tasks", "3.3.4 Exam Tasks"),
    "kunpeng": ("3.3.4 Exam Tasks", None),
}


def extract_cache_path(lab_name: str) -> Path:
    return OUTPUT_DIR / f"{(lab_name or 'lab').strip() or 'lab'}_extract.md"


def _pdf_to_markdown(pdf_path: Path) -> str:
    doc = fitz.open(pdf_path)
    parts = [f"# Lab extraido de {pdf_path.name}\n"]
    for i, page in enumerate(doc):
        text = page.get_text().strip()
        parts.append(f"\n## Pagina {i + 1}\n\n{text if text else '_(sin texto)_'}\n")
    doc.close()
    return "\n".join(parts).strip() + "\n"


def _slice_section(full_text: str, section: str) -> str:
    start_label, end_label = _SECTION_BOUNDS[section]
    starts = [m.start() for m in re.finditer(re.escape(start_label), full_text)]
    if not starts:
        return full_text
    start = starts[-1]
    if end_label:
        end = len(full_text)
        for m in re.finditer(re.escape(end_label), full_text):
            if m.start() > start:
                end = m.start()
                break
    else:
        end = len(full_text)
    block = full_text[start:end].strip()
    return block if block else full_text


def load_or_extract(pdf_path: Path, lab_name: str, section: str | None = None) -> str:
    cache = extract_cache_path(lab_name)
    if cache.is_file() and cache.stat().st_mtime_ns >= pdf_path.stat().st_mtime_ns:
        full = cache.read_text(encoding="utf-8")
        print(f"[extract] cache {cache.name} ({len(full) // 1024} KB)", flush=True)
    else:
        print(f"[extract] PDF -> markdown local ({pdf_path.name})...", flush=True)
        full = _pdf_to_markdown(pdf_path)
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(full, encoding="utf-8")
        print(f"[extract] guardado {cache.name} ({len(full) // 1024} KB)", flush=True)

    if section:
        sliced = _slice_section(full, section)
        print(f"[extract] seccion {section}: {len(sliced) // 1024} KB (de {len(full) // 1024} KB)", flush=True)
        return sliced
    return full
