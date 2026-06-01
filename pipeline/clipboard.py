import subprocess
import sys


def copy(text: str) -> bool:
    if not text.strip():
        return False
    if sys.platform == "win32":
        p = subprocess.Popen(
            ["clip"],
            stdin=subprocess.PIPE,
            shell=True,
        )
        p.communicate(input=text.encode("utf-16le"))
        return p.returncode == 0
    try:
        subprocess.run(["xclip", "-selection", "clipboard"], input=text.encode(), check=True)
        return True
    except Exception:
        return False
