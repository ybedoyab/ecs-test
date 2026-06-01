from pipeline.context_store import all_ready, is_ready, load_knowledge
from pipeline.sections import SECTIONS


def check_context() -> bool:
    ok = True
    for section in SECTIONS:
        if is_ready(section):
            print(f"  {section}: ok")
        else:
            print(f"  {section}: FALTA knowledge.md")
            ok = False
    return ok and all_ready()


def ensure_ready(section: str) -> str:
    if not is_ready(section):
        raise FileNotFoundError(
            f"Contexto '{section}' no disponible. Verifica context/{section}/knowledge.md"
        )
    return load_knowledge(section)
