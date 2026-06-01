import sys
from pathlib import Path

from config import ANSWERS_DIR, ANTHROPIC_API_KEY, DEFAULT_NAME, PROMPTS_DIR, answers_path
from pipeline import claude_client
from pipeline.pdf_source import resolve_pdf


def main():
    name = (sys.argv[1] if len(sys.argv) > 1 else DEFAULT_NAME).strip() or "lab"
    source = resolve_pdf(name)
    if not source:
        print(f"No hay PDF para '{name}'.")
        print(f"Coloca Regional_2526_Lab_ocr.pdf en Scripts/ o corre: python main.py {name}")
        sys.exit(1)

    ANSWERS_DIR.mkdir(parents=True, exist_ok=True)
    out = answers_path(name)
    prompt_file = PROMPTS_DIR / "claude_lab.md"
    system = prompt_file.read_text(encoding="utf-8")

    if not ANTHROPIC_API_KEY:
        out.write_text(
            f"# {name}\n\nFalta ANTHROPIC_API_KEY en .env\nFuente: {source.name}\n",
            encoding="utf-8",
        )
        print(f"Sin API key. Placeholder: {out}")
        sys.exit(0)

    print(f"Enviando {source.name} a Claude...")
    md = claude_client.pdf_markdown(ANTHROPIC_API_KEY, system, source)
    if "<!-- TASK:" not in md:
        md = f"# {name}\n\n{md}"
    out.write_text(md, encoding="utf-8")
    print(f"Guardado: {out}")


if __name__ == "__main__":
    main()
