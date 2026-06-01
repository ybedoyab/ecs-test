from pathlib import Path

from config import ANSWERS_DIR, answers_path
from pipeline.sections import extract_section


def _answer_files() -> list[Path]:
    ordered: list[Path] = []
    seen: set[Path] = set()
    primary = answers_path()
    if primary.is_file():
        ordered.append(primary)
        seen.add(primary.resolve())
    for path in sorted(ANSWERS_DIR.glob("*.md")):
        key = path.resolve()
        if key in seen:
            continue
        ordered.append(path)
        seen.add(key)
    return ordered


def load_lab_context(section: str) -> tuple[str, str | None]:
    """Tareas del lab para una seccion. Devuelve (texto, nombre_archivo_fuente)."""
    for path in _answer_files():
        try:
            md = path.read_text(encoding="utf-8")
        except OSError:
            continue
        block = extract_section(md, section)
        if block:
            return block, path.name
    return "", None
