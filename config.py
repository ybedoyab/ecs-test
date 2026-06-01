from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent
_env = ROOT / ".env"
if _env.exists():
    for line in _env.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

CURL_FILE = ROOT / "curl_comando.txt"
TEST_OCR_PDF = ROOT / "test" / "Regional_2526_Lab_ocr.pdf"
OUTPUT_DIR = ROOT / "output"
SLIDES_DIR = OUTPUT_DIR / "_slides"
TASKS_DIR = ROOT / "tasks"
ANSWERS_DIR = ROOT / "answers"
CONTEXT_DIR = ROOT / "context"

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
PROMPTS_DIR = ROOT / "prompts"
DEFAULT_NAME = (os.getenv("LAB_NAME") or "lab").strip() or "lab"


def answers_path(lab_name: str | None = None) -> Path:
    return ANSWERS_DIR / f"{(lab_name or DEFAULT_NAME).strip() or 'lab'}.md"
