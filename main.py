import sys
from pathlib import Path

from config import CURL_FILE, DEFAULT_NAME, OUTPUT_DIR, SLIDES_DIR
from pipeline import claude_run, compress, download, ocr
from pipeline.sections import normalize_section


def _parse_args(argv: list[str]) -> tuple[str, str | None]:
    name = DEFAULT_NAME
    section = None
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg == "--claude":
            if i + 1 >= len(argv):
                print("Uso: python main.py [--claude openeuler|opengauss|kunpeng] [nombre_lab]")
                sys.exit(1)
            section = normalize_section(argv[i + 1])
            i += 2
            continue
        if arg.startswith("-"):
            print(f"Opcion desconocida: {arg}")
            sys.exit(1)
        name = arg.strip() or "lab"
        i += 1
    return name, section


def _run_pipeline(name: str) -> None:
    if not CURL_FILE.exists():
        print(f"Crea {CURL_FILE} con el curl copiado del navegador")
        sys.exit(1)
    curl = CURL_FILE.read_text(encoding="utf-8")
    if "curl" not in curl.lower():
        print("curl_comando.txt no contiene un curl valido")
        sys.exit(1)

    base = OUTPUT_DIR / name
    pdf = base.with_suffix(".pdf")
    ocr_pdf = Path(str(pdf).replace(".pdf", "_ocr.pdf"))
    small_pdf = Path(str(pdf).replace(".pdf", "_small.pdf"))

    print("=== 1/3 Descarga ===")
    download.run(curl, SLIDES_DIR, pdf)

    print("=== 2/3 OCR ===")
    ocr.run(pdf, ocr_pdf)

    print("=== 3/3 Compresion ===")
    compress.run(ocr_pdf, small_pdf)

    print(f"\nListo:\n  {pdf}\n  {ocr_pdf}\n  {small_pdf}")


def main():
    name, section = _parse_args(sys.argv[1:])
    if section:
        try:
            claude_run.run(name, section)
        except FileNotFoundError as e:
            print(e)
            sys.exit(1)
        return
    _run_pipeline(name)


if __name__ == "__main__":
    main()
