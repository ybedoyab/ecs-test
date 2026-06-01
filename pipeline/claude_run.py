from pathlib import Path

from config import ANSWERS_DIR, ANTHROPIC_API_KEY, PROMPTS_DIR, answers_path
from pipeline import claude_client
from pipeline.context_store import is_ready, load_knowledge
from pipeline.pdf_source import resolve_pdf
from pipeline.pdf_text import load_or_extract
from pipeline.sections import SECTIONS, merge_section, normalize_section, strip_code_fence


def _build_prompt(section: str) -> str:
    meta = SECTIONS[section]
    base = (PROMPTS_DIR / "claude_lab.md").read_text(encoding="utf-8")
    extra = (PROMPTS_DIR / f"claude_{section}.md").read_text(encoding="utf-8")
    prompt = (
        f"{base}\n\n"
        f"=== FILTRO DE SECCION: {meta['title']} ===\n"
        f"{meta['pdf_hint']}\n"
        f"IDs obligatorios: {meta['id_rule']}\n"
        f"Prefijo de tarea: {meta['id_prefix']}\n\n"
        f"{extra}\n"
        f"Genera SOLO las tareas de {meta['title']}. Nada de otras secciones.\n"
    )
    if is_ready(section):
        prompt += f"\n=== CONOCIMIENTO ENTRENADO ===\n{load_knowledge(section)}\n"
    return prompt


def run(name: str, section: str | None = None) -> Path:
    lab = (name or "lab").strip() or "lab"
    source = resolve_pdf(lab)
    if not source:
        raise FileNotFoundError(
            f"No hay PDF para '{lab}'. Coloca el PDF en Scripts/ o corre main.py {lab}"
        )

    ANSWERS_DIR.mkdir(parents=True, exist_ok=True)
    out = answers_path(lab)
    sec = normalize_section(section) if section else None

    if not ANTHROPIC_API_KEY:
        placeholder = f"Falta ANTHROPIC_API_KEY en .env\nFuente: {source.name}\n"
        if sec:
            existing = out.read_text(encoding="utf-8") if out.exists() else f"# {lab}\n"
            out.write_text(merge_section(existing, sec, placeholder), encoding="utf-8")
        else:
            out.write_text(f"# {lab}\n\n{placeholder}", encoding="utf-8")
        return out

    system = _build_prompt(sec) if sec else (PROMPTS_DIR / "claude_lab.md").read_text(encoding="utf-8")
    label = f"{lab}/{sec}" if sec else lab
    print(f"\n--- {label} ({source.name}) ---", flush=True)
    lab_text = load_or_extract(source, lab, sec)
    user = (
        "Contenido del lab (texto extraido del PDF, por paginas). "
        "Genera el markdown de tareas segun el formato del system.\n\n"
        f"{lab_text}"
    )
    md = strip_code_fence(
        claude_client.text(ANTHROPIC_API_KEY, system, user, max_tokens=16384, stream=True)
    )

    if sec:
        existing = out.read_text(encoding="utf-8") if out.exists() else f"# {lab}\n"
        out.write_text(merge_section(existing, sec, md), encoding="utf-8")
    else:
        if "<!-- TASK:" not in md and "<!-- SECTION:" not in md:
            md = f"# {lab}\n\n{md}"
        out.write_text(md, encoding="utf-8")

    print(f"Guardado: {out}")
    return out
