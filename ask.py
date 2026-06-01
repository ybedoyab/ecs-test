import sys

from config import ANTHROPIC_API_KEY, PROMPTS_DIR
from pipeline import claude_client
from pipeline.context_train import ensure_ready
from pipeline.lab_context import load_lab_context
from pipeline.sections import SECTIONS, normalize_section


def main():
    if len(sys.argv) < 2:
        print("Uso: python ask.py openeuler|opengauss|kunpeng")
        sys.exit(1)
    try:
        section = normalize_section(sys.argv[1])
    except ValueError as e:
        print(e)
        sys.exit(1)

    try:
        knowledge = ensure_ready(section)
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)

    title = SECTIONS[section]["title"]
    base = (PROMPTS_DIR / "claude_ask.md").read_text(encoding="utf-8")
    lab_block, lab_source = load_lab_context(section)
    system = f"{base}\n\n"
    if lab_block:
        system += f"=== LAB / TAREAS OFICIALES ({title}) — {lab_source} ===\n{lab_block}\n\n"
    else:
        print(
            f"Aviso: no hay bloque <!-- SECTION:{section} --> en answers/. "
            f"Genera respuestas (p. ej. python claude.py regional_2526 {section}) "
            f"o edita answers/*.md\n"
        )
    system += f"=== CONOCIMIENTO ENTRENADO ({title}) ===\n{knowledge}\n"

    if not ANTHROPIC_API_KEY:
        print(f"Chat {section} (sin API key). Contexto cargado: {len(knowledge)} chars")
        print("Define ANTHROPIC_API_KEY en .env")
        sys.exit(0)

    lab_note = f"lab={lab_source}" if lab_source else "lab=sin tareas en answers/"
    print(f"Chat {section} — {lab_note}, curso={len(knowledge)} chars. Escribe tu duda (q=salir)\n")
    history: list[dict] = []
    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not line or line.lower() in ("q", "quit", "exit", "salir"):
            break
        history.append({"role": "user", "content": line})
        try:
            print()
            reply = claude_client.chat(ANTHROPIC_API_KEY, system, history, max_tokens=2048, stream=True)
        except Exception as e:
            print(f"\nError: {e}", flush=True)
            history.pop()
            continue
        if reply and not reply.endswith("\n"):
            print()
        history.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
