import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from config import answers_path
from pipeline.task_parse import extract_task, load_answers, normalize_task_id


def main():
    lab = (sys.argv[1] if len(sys.argv) > 1 else "regional_2526").strip()
    task = sys.argv[2] if len(sys.argv) > 2 else "1.1"
    md = load_answers(answers_path(lab))
    tid = normalize_task_id(task)
    block = extract_task(md, tid)
    if not block:
        print(f"FAIL: {tid} no encontrado en {lab}")
        sys.exit(1)
    print(f"OK {tid}: {block.title}")
    print(f"  screenshots: {len(block.screenshots)}")
    print(f"  copy chars: {len(block.copy_text)}")
    for s in block.screenshots:
        print(f"    {s}")


if __name__ == "__main__":
    main()
