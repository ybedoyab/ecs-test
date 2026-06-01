import sys
from pathlib import Path

from config import ANTHROPIC_API_KEY, DEFAULT_NAME, PROMPTS_DIR, answers_path
from pipeline import claude_client
from pipeline.task_parse import extract_task, load_answers, normalize_task_id


def main():
    if len(sys.argv) < 3:
        print("Uso: python ask.py task1_1 ask.txt [lab]")
        sys.exit(1)
    try:
        task_id = normalize_task_id(sys.argv[1])
    except ValueError as e:
        print(e)
        sys.exit(1)
    ask_file = Path(sys.argv[2])
    if not ask_file.is_file():
        print(f"No existe: {ask_file}")
        sys.exit(1)
    lab = (sys.argv[3] if len(sys.argv) > 3 else DEFAULT_NAME).strip() or "lab"
    question = ask_file.read_text(encoding="utf-8").strip()
    if not question:
        print("ask.txt vacio")
        sys.exit(1)

    md_file = answers_path(lab)
    try:
        md = load_answers(md_file)
    except FileNotFoundError:
        print(f"No existe {md_file}. Ejecuta: python claude.py {lab}")
        sys.exit(1)

    block = extract_task(md, task_id)
    if not block:
        print(f"Tarea {task_id} no esta en {md_file.name}")
        sys.exit(1)

    system = (PROMPTS_DIR / "claude_ask.md").read_text(encoding="utf-8")
    shots = "\n".join(f"- {s}" for s in block.screenshots) or "(ninguno)"
    user = (
        f"Tarea: {task_id}\n"
        f"Titulo: {block.title}\n\n"
        f"Bloque oficial copy:\n{block.copy_text}\n\n"
        f"Screenshots esperados:\n{shots}\n\n"
        f"Duda / error del estudiante:\n{question}"
    )

    if not ANTHROPIC_API_KEY:
        print(f"--- ask {task_id} (sin API key) ---\n")
        print(f"Tarea: {block.title or task_id}")
        print(f"Pregunta: {question}\n")
        print("Define ANTHROPIC_API_KEY en .env para respuesta de Claude.")
        sys.exit(0)

    print(f"Consultando Claude sobre {task_id}...")
    answer = claude_client.text(ANTHROPIC_API_KEY, system, user, max_tokens=2048)
    print()
    print(answer)


if __name__ == "__main__":
    main()
