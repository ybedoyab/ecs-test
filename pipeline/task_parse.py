import re
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class TaskStep:
    copy_text: str = ""
    screenshot: str = ""


@dataclass
class TaskBlock:
    task_id: str
    title: str = ""
    steps: list[TaskStep] = field(default_factory=list)
    screenshots: list[str] = field(default_factory=list)
    copy_text: str = ""
    files: list[str] = field(default_factory=list)


def normalize_task_id(raw: str) -> str:
    s = raw.strip().lower().replace("-", "_").replace(".", "_")
    s = re.sub(r"^task", "", s)
    m = re.match(r"^([tgk])(\d+)_(\d+)$", s)
    if m:
        return f"{m.group(1)}{m.group(2)}_{m.group(3)}"
    m = re.match(r"^t?(\d+)_(\d+)$", s)
    if m:
        return f"t{m.group(1)}_{m.group(2)}"
    m = re.match(r"^(\d+)_(\d+)$", s)
    if m:
        return f"t{m.group(1)}_{m.group(2)}"
    raise ValueError(f"ID de tarea no reconocido: {raw}")


def screenshot_name(task_id: str, slug: str) -> str:
    slug = re.sub(r"^screenshot\s+", "", slug.strip(), flags=re.I)
    if re.match(r"^\d+-\d+-[\w]", slug):
        return slug
    m = re.match(r"^([tgk])(\d+)_(\d+)", task_id)
    if m:
        return f"{m.group(2)}-{m.group(3)}-{slug}" if not re.match(r"^\d+-\d+", slug) else slug
    m = re.match(r"t(\d+)_(\d+)", task_id)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{slug}"
    return slug


def _read_fence(lines: list[str], start: int) -> tuple[str, int]:
    i = start
    while i < len(lines) and not lines[i].strip().startswith("```"):
        i += 1
    if i >= len(lines):
        return "", start
    i += 1
    buf: list[str] = []
    while i < len(lines) and not lines[i].strip().startswith("```"):
        buf.append(lines[i])
        i += 1
    return "\n".join(buf).strip(), i + 1


def _finalize(block: TaskBlock) -> TaskBlock:
    if block.steps:
        block.screenshots = [s.screenshot for s in block.steps if s.screenshot]
        block.copy_text = "\n".join(s.copy_text for s in block.steps if s.copy_text).strip()
    return block


def _parse_steps(task_id: str, body: str) -> list[TaskStep]:
    chunks = re.split(r"^step:\s*$", body, flags=re.I | re.MULTILINE)
    steps: list[TaskStep] = []
    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk or chunk.startswith("#"):
            continue
        lines = chunk.splitlines()
        i = 0
        step = TaskStep()
        while i < len(lines):
            low = lines[i].strip().lower()
            if low == "copy:":
                step.copy_text, i = _read_fence(lines, i + 1)
                continue
            if low.startswith("captura:") or low.startswith("screenshot:"):
                raw = lines[i].split(":", 1)[1].strip()
                if raw.startswith("- "):
                    raw = raw[2:].strip()
                step.screenshot = screenshot_name(task_id, raw)
                i += 1
                continue
            i += 1
        if step.copy_text or step.screenshot:
            steps.append(step)
    return steps


def _parse_block_body(task_id: str, body: str) -> TaskBlock:
    block = TaskBlock(task_id=task_id)
    lines = body.splitlines()
    i = 0
    if i < len(lines) and lines[i].startswith("#"):
        block.title = lines[i].lstrip("#").strip()
        i += 1

    rest = "\n".join(lines[i:])
    block.steps = _parse_steps(task_id, rest)
    if block.steps:
        return _finalize(block)

    section = None
    copy_lines: list[str] = []
    in_fence = False
    i = 0
    lines = rest.splitlines()

    while i < len(lines):
        line = lines[i]
        low = line.strip().lower()

        if low in ("screenshots:", "screenshot:"):
            section = "screenshots"
            i += 1
            continue
        if low == "copy:":
            section = "copy"
            i += 1
            continue
        if low == "files:":
            section = "files"
            i += 1
            continue

        if section == "screenshots":
            if low.startswith("- "):
                item = line.strip()[2:].strip()
                if item:
                    block.screenshots.append(screenshot_name(task_id, item))
            elif line.strip() and not line.strip().endswith(":"):
                block.screenshots.append(screenshot_name(task_id, line.strip()))
            i += 1
            continue

        if section == "files":
            if low.startswith("- "):
                block.files.append(line.strip()[2:].strip())
            i += 1
            continue

        if section == "copy":
            if line.strip().startswith("```"):
                if in_fence:
                    in_fence = False
                    section = None
                else:
                    in_fence = True
                i += 1
                continue
            if in_fence:
                copy_lines.append(line)
            i += 1
            continue

        i += 1

    block.copy_text = "\n".join(copy_lines).strip()
    if block.copy_text and block.screenshots:
        cmds = [c.strip() for c in block.copy_text.split("\n") if c.strip()]
        if len(cmds) == len(block.screenshots):
            block.steps = [
                TaskStep(copy_text=cmd, screenshot=shot)
                for cmd, shot in zip(cmds, block.screenshots)
            ]
        else:
            block.steps = [TaskStep(copy_text=block.copy_text, screenshot=block.screenshots[0])]
            for shot in block.screenshots[1:]:
                block.steps.append(TaskStep(screenshot=shot))
    elif block.copy_text:
        block.steps = [TaskStep(copy_text=block.copy_text)]
    elif block.screenshots:
        block.steps = [TaskStep(screenshot=s) for s in block.screenshots]

    return _finalize(block)


def extract_task(md_text: str, task_id: str) -> TaskBlock | None:
    tid = normalize_task_id(task_id)
    pat = re.compile(
        rf"<!--\s*TASK:{re.escape(tid)}\s*-->(.*?)<!--\s*END:{re.escape(tid)}\s*-->",
        re.DOTALL | re.IGNORECASE,
    )
    m = pat.search(md_text)
    if m:
        return _parse_block_body(tid, m.group(1).strip())

    pat2 = re.compile(
        rf"^##\s*TASK\s+{re.escape(tid)}\s*$([\s\S]*?)(?=^##\s*TASK\s+t\d+_\d+\s*$|\Z)",
        re.MULTILINE | re.IGNORECASE,
    )
    m2 = pat2.search(md_text)
    if m2:
        return _parse_block_body(tid, m2.group(1).strip())
    return None


def load_answers(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8")
