import sys
from pathlib import Path

from config import CURL_FILE, DEFAULT_NAME, OUTPUT_DIR, SLIDES_DIR
from pipeline import compress, download, ocr


def main():
    name = (sys.argv[1] if len(sys.argv) > 1 else DEFAULT_NAME).strip() or "lab"
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


if __name__ == "__main__":
    main()
