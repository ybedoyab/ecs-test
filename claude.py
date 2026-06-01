import sys

from config import DEFAULT_NAME
from pipeline import claude_run
from pipeline.sections import normalize_section


def main():
    name = DEFAULT_NAME
    section = None
    for arg in sys.argv[1:]:
        arg = arg.strip()
        if not arg:
            continue
        try:
            section = normalize_section(arg)
        except ValueError:
            name = arg or name
    try:
        claude_run.run(name, section)
    except (FileNotFoundError, ValueError) as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
