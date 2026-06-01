import shutil
import sys
from pathlib import Path

from config import ANTHROPIC_API_KEY, CURL_FILE, DEFAULT_NAME, OUTPUT_DIR, SLIDES_DIR, TEST_OCR_PDF
from pipeline import claude_run, compress, download, ocr
from pipeline.context_train import check_context
from pipeline.sections import SECTIONS


def _paths(name: str):
    base = OUTPUT_DIR / name
    pdf = base.with_suffix(".pdf")
    ocr_pdf = Path(str(pdf).replace(".pdf", "_ocr.pdf"))
    small_pdf = Path(str(pdf).replace(".pdf", "_small.pdf"))
    return pdf, ocr_pdf, small_pdf


def _resolve_lab(name: str) -> None:
    print("\n=== Resolviendo lab (Claude) ===")
    if not ANTHROPIC_API_KEY:
        print("  Sin ANTHROPIC_API_KEY: salta generacion de answers/")
        return
    for section in SECTIONS:
        print(f"  {section}...")
        try:
            claude_run.run(name, section)
        except Exception as e:
            print(f"  [error] {section}: {e}")


def _print_next_steps(name: str) -> None:
    print(f"""
=== Listo - usa estos comandos ===
  python copy_task.py t1_1 {name} --print    openEuler (pega texto al portapapeles)
  python copy_task.py g1_1 {name}            openGauss
  python copy_task.py k1_1 {name}            Kunpeng
  python ask.py openeuler                     chat con dudas
  python ask.py opengauss
  python ask.py kunpeng
  python claude.py {name} openeuler           regenerar solo una seccion

Respuestas: answers/{name}.md
PDF: output/{name}_small.pdf
""")


def _run_pipeline(name: str) -> None:
    if not CURL_FILE.exists():
        print(f"Crea {CURL_FILE} con el curl copiado del navegador")
        sys.exit(1)
    curl = CURL_FILE.read_text(encoding="utf-8")
    if "curl" not in curl.lower():
        print("curl_comando.txt no contiene un curl valido")
        sys.exit(1)

    pdf, ocr_pdf, small_pdf = _paths(name)

    print("=== 1/3 Descarga ===")
    download.run(curl, SLIDES_DIR, pdf)

    print("=== 2/3 OCR ===")
    ocr.run(pdf, ocr_pdf)

    print("=== 3/3 Compresion ===")
    compress.run(ocr_pdf, small_pdf)

    print(f"\nPDF: {pdf}\n     {ocr_pdf}\n     {small_pdf}")
    _resolve_lab(name)
    _print_next_steps(name)


def _run_test_pipeline(name: str) -> None:
    try:
        if not TEST_OCR_PDF.is_file():
            print(f"[test] no existe: {TEST_OCR_PDF}")
            sys.exit(1)
        print(f"[test] origen: {TEST_OCR_PDF.name}")
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        pdf, ocr_pdf, small_pdf = _paths(name)
        shutil.copy2(TEST_OCR_PDF, pdf)
        shutil.copy2(TEST_OCR_PDF, ocr_pdf)
        print(f"[test] copiado -> {pdf.name}, {ocr_pdf.name}")
        print("[test] comprimiendo...")
        compress.run(ocr_pdf, small_pdf)
        if not small_pdf.is_file() or small_pdf.stat().st_size < 1000:
            print(f"[test] compresion fallo: {small_pdf}")
            sys.exit(1)
        mb = small_pdf.stat().st_size / (1024 * 1024)
        print(f"[test] listo: {small_pdf.name} ({mb:.2f} MB)")
        _resolve_lab(name)
        _print_next_steps(name)
    except Exception as e:
        print(f"[test] error: {e}")
        sys.exit(1)


def main():
    name = DEFAULT_NAME
    skip_pipeline = "--train-only" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if args:
        name = args[0].strip() or name

    print("=== Verificando contexto ===")
    if not check_context():
        print("\nFalta context/ en alguna seccion. Restaura el repo o pide el context/ al equipo.")
        sys.exit(1)

    print("\nContexto listo. Chats: python ask.py openeuler | opengauss | kunpeng")

    if skip_pipeline:
        return

    try:
        ans = input("\nQuiere proceder con el pipeline? (s/n/t=test): ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print()
        return

    if ans == "t":
        _run_test_pipeline(name)
        return

    if ans not in ("s", "si", "y", "yes"):
        print("Pipeline omitido.")
        return

    _run_pipeline(name)


if __name__ == "__main__":
    main()
