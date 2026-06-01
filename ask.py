import sys

from config import ANTHROPIC_API_KEY, PROMPTS_DIR
from pipeline import claude_client
from pipeline.context_train import ensure_ready
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
    system = (
        f"{base}\n\n"
        f"=== CONOCIMIENTO ENTRENADO ({title}) ===\n"
        f"{knowledge}\n"
    )

    if not ANTHROPIC_API_KEY:
        print(f"Chat {section} (sin API key). Contexto cargado: {len(knowledge)} chars")
        print("Define ANTHROPIC_API_KEY en .env")
        sys.exit(0)

    print(f"Chat {section} — contexto compartido. Escribe tu duda (q=salir)\n")
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
            reply = claude_client.chat(ANTHROPIC_API_KEY, system, history, max_tokens=2048)
        except Exception as e:
            print(f"Error: {e}")
            history.pop()
            continue
        print(f"\n{reply}\n")
        history.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
