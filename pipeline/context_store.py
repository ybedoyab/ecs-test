import hashlib
import json
import os
import time
from pathlib import Path

from config import CONTEXT_DIR, PROMPTS_DIR
from pipeline.sections import SECTIONS

LOCK_FILE = CONTEXT_DIR / ".train.lock"
PROMPT_TRAIN = PROMPTS_DIR / "context_train.md"


def section_dir(section: str) -> Path:
    d = CONTEXT_DIR / section
    d.mkdir(parents=True, exist_ok=True)
    return d


def ready_path(section: str) -> Path:
    return section_dir(section) / "ready"


def knowledge_path(section: str) -> Path:
    return section_dir(section) / "knowledge.md"


def fingerprint_path(section: str) -> Path:
    return section_dir(section) / "sources.json"


def is_ready(section: str) -> bool:
    return ready_path(section).is_file() and knowledge_path(section).is_file()


def all_ready() -> bool:
    return all(is_ready(s) for s in SECTIONS)


def load_knowledge(section: str) -> str:
    p = knowledge_path(section)
    if not p.is_file():
        raise FileNotFoundError(
            f"Contexto no entrenado para {section}. Ejecuta: python main.py"
        )
    return p.read_text(encoding="utf-8")


def save_knowledge(section: str, text: str, files: list[Path]) -> None:
    knowledge_path(section).write_text(text.strip() + "\n", encoding="utf-8")
    data = {
        "sources": [p.name for p in files],
        "hash": sources_fingerprint(files),
        "ts": time.time(),
    }
    fingerprint_path(section).write_text(json.dumps(data, indent=2), encoding="utf-8")
    ready_path(section).write_text(str(time.time()), encoding="utf-8")


def sources_fingerprint(files: list[Path]) -> str:
    h = hashlib.sha256()
    for p in files:
        st = p.stat()
        h.update(f"{p.name}:{st.st_size}:{st.st_mtime_ns}".encode())
    return h.hexdigest()


def needs_retrain(section: str, files: list[Path]) -> bool:
    if not is_ready(section):
        return True
    fp = fingerprint_path(section)
    if not fp.is_file():
        return True
    try:
        old = json.loads(fp.read_text(encoding="utf-8"))
        old_sources = old.get("sources", [])
    except Exception:
        return True
    new_sources = [p.name for p in files]
    if sorted(old_sources) != sorted(new_sources):
        return True
    old_hash = old.get("hash")
    return old_hash != sources_fingerprint(files)


def mark_sources(section: str, files: list[Path]) -> None:
    data = {
        "sources": [p.name for p in files],
        "hash": sources_fingerprint(files),
        "ts": time.time(),
    }
    fingerprint_path(section).write_text(json.dumps(data, indent=2), encoding="utf-8")


class TrainLock:
    def __init__(self, timeout: float = 600):
        self.timeout = timeout
        self.handle = None

    def __enter__(self):
        CONTEXT_DIR.mkdir(parents=True, exist_ok=True)
        self.handle = open(LOCK_FILE, "a+")
        start = time.time()
        while True:
            try:
                if os.name == "nt":
                    import msvcrt
                    msvcrt.locking(self.handle.fileno(), msvcrt.LK_NBLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(self.handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                return self
            except (OSError, BlockingIOError):
                if time.time() - start > self.timeout:
                    raise TimeoutError("Otro usuario esta entrenando el contexto")
                time.sleep(2)

    def __exit__(self, *args):
        if self.handle:
            try:
                if os.name == "nt":
                    import msvcrt
                    msvcrt.locking(self.handle.fileno(), msvcrt.LK_UNLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(self.handle.fileno(), fcntl.LOCK_UN)
            except Exception:
                pass
            self.handle.close()
