import shutil
import sys
from pathlib import Path

from config import DEFAULT_NAME, TASKS_DIR, answers_path
from pipeline.clipboard import copy as clip_copy
from pipeline.task_parse import extract_task, load_answers, normalize_task_id


def _collect_steps(block) -> str:
    parts: list[str] = []
    for step in block.steps:
        if step.copy_text:
            parts.append(step.copy_text)
    return "\n".join(parts).strip()


def _print_steps(block) -> None:
    for n, step in enumerate(block.steps, 1):
        print(f"--- Paso {n} ---")
        if step.copy_text:
            print("Comandos:")
            print(step.copy_text)
        if step.screenshot:
            print(f"Captura: {step.screenshot}")
        print()


def main():
    raw = sys.argv[1:]
    do_print = "--print" in raw
    args = [a for a in raw if a != "--print"]
    if not args:
        print("Uso: python copy_task.py task1_1 [lab] [--print]")
        sys.exit(1)
    try:
        task_id = normalize_task_id(args[0])
    except ValueError as e:
        print(e)
        sys.exit(1)
    lab = (args[1] if len(args) > 1 else DEFAULT_NAME).strip() or "lab"
    md_file = answers_path(lab)

    try:
        md = load_answers(md_file)
    except FileNotFoundError:
        print(f"No existe {md_file}. Ejecuta: python claude.py {lab}")
        sys.exit(1)

    block = extract_task(md, task_id)
    if not block:
        print(f"Tarea {task_id} no encontrada en {md_file.name}")
        sys.exit(1)
    if not block.steps:
        print(f"{task_id}: sin pasos en el markdown")
        sys.exit(1)

    combined = _collect_steps(block)
    if combined:
        clip_copy(combined)

    if do_print:
        print(f"\n=== {task_id} ===")
        if block.title:
            print(block.title)
        print()
        _print_steps(block)
        if combined:
            print(f"(portapapeles: {len(combined)} caracteres)")

    task_dir = TASKS_DIR / task_id
    for rel in block.files:
        rel = rel.replace("\\", "/").lstrip("/")
        src = task_dir / rel
        if not src.is_file():
            if do_print:
                print(f"omitido: tasks/{task_id}/{rel}")
            continue
        dest = Path.cwd() / src.name
        shutil.copy2(src, dest)
        if do_print:
            print(f"archivo: {dest.name}")


if __name__ == "__main__":
    main()
