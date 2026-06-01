import re

SECTIONS = {
    "openeuler": {
        "title": "openEuler",
        "pdf_hint": "Seccion 3.1 openEuler Tasks del PDF (3.1.5 Exam Tasks). Ignora openGauss y Kunpeng.",
        "id_prefix": "t",
        "id_rule": "TASK:t{task}_{subtask} — Task 1 Subtask 1 = t1_1, Task 2 Subtask 1 = t2_1",
    },
    "opengauss": {
        "title": "openGauss",
        "pdf_hint": "Seccion 3.2 openGauss Tasks del PDF (3.2.4 Exam Tasks). Ignora openEuler y Kunpeng.",
        "id_prefix": "g",
        "id_rule": "TASK:g{task}_{subtask} — Task 1 Subtask 1 = g1_1, Task 2 Subtask 1 = g2_1",
    },
    "kunpeng": {
        "title": "Kunpeng",
        "pdf_hint": "Seccion 3.3 Kunpeng Application Development Tasks del PDF (3.3.4 Exam Tasks). Ignora openEuler y openGauss.",
        "id_prefix": "k",
        "id_rule": "TASK:k{task}_{subtask} — Task 1 Subtask 1 = k1_1",
    },
}

ALIASES = {
    "open_euler": "openeuler",
    "euler": "openeuler",
    "gauss": "opengauss",
    "open_gauss": "opengauss",
    "kp": "kunpeng",
}


def normalize_section(raw: str) -> str:
    key = raw.strip().lower().replace("-", "").replace("_", "")
    if key in ALIASES:
        key = ALIASES[key]
    if key not in SECTIONS:
        raise ValueError(f"Seccion invalida: {raw}. Usa: openeuler, opengauss, kunpeng")
    return key


def section_marker(section: str, end: bool = False) -> str:
    tag = f"END:{section}" if end else f"SECTION:{section}"
    return f"<!-- {tag} -->"


def merge_section(existing: str, section: str, body: str) -> str:
    start = section_marker(section)
    end = section_marker(section, end=True)
    block = f"{start}\n{body.strip()}\n{end}"
    if start in existing:
        pat = re.compile(
            re.escape(start) + r"[\s\S]*?" + re.escape(end),
            re.MULTILINE,
        )
        return pat.sub(block, existing)
    base = existing.rstrip()
    if base:
        return f"{base}\n\n{block}\n"
    return f"# lab\n\n{block}\n"


def strip_code_fence(md: str) -> str:
    text = md.strip()
    m = re.match(r"^```(?:markdown|md)?\s*\n([\s\S]*?)\n```\s*$", text)
    return m.group(1).strip() if m else text
