import os
import sys
import io
import threading
import queue
import time
import logging

# EasyOCR importa Torch y puede tardar minutos SIN imprimir nada: no importar al cargar el módulo.
def _boot_print(msg: str) -> None:
    print(msg, flush=True)


_boot_print("ocr_converter.py: iniciando (importando PyMuPDF, NumPy, Pillow...)")

import fitz  # PyMuPDF
import numpy as np
from PIL import Image

_boot_print("ocr_converter.py: dependencias ligeras OK. EasyOCR se carga al empezar el OCR.")

try:
    sys.stdout.reconfigure(line_buffering=True)  # Python 3.7+: ver líneas al instante en PowerShell
except Exception:
    pass

# ==========================================
# LOG en consola + archivo
# ==========================================
class _FlushStreamHandler(logging.StreamHandler):
    def emit(self, record):
        super().emit(record)
        self.flush()


def _setup_logging():
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    root.handlers.clear()
    fmt = logging.Formatter("%(asctime)s | %(message)s", datefmt="%H:%M:%S")
    sh = _FlushStreamHandler(sys.stdout)
    sh.setFormatter(fmt)
    root.addHandler(sh)


def log_msg(msg):
    """Salida por consola vía logging."""
    logging.info(msg)


# ==========================================
# CONFIGURACIÓN
# ==========================================
MODO_TURBO_HILOS = 4  
BUFFER_IMAGENES = 15  
REINTENTOS_PAGINA = 3
SALTAR_EXISTENTES = True 

# Configuración de Compresión (Igual que pdf_merger.py)
CALIDAD_JPEG = 75  # 1-100
REDUCIR_RESOLUCION = True 
MAX_WIDTH = 1280

_setup_logging()

def agregar_ocr_a_pdf(input_pdf, reader):
    output_pdf = input_pdf.replace(".pdf", "_ocr.pdf")
    
    if SALTAR_EXISTENTES and os.path.exists(output_pdf):
        log_msg(f"Saltando {input_pdf} (ya existe _ocr.pdf). Borra el _ocr para regenerar.")
        return True

    print(f"\n" + "="*50, flush=True)
    print(f"  PROCESANDO: {os.path.basename(input_pdf)}", flush=True)
    print("="*50, flush=True)
    log_msg(f"Iniciando OCR para: {os.path.abspath(input_pdf)}")
    
    try:
        doc = fitz.open(input_pdf)
    except Exception as e:
        log_msg(f"ERROR abriendo PDF: {e}")
        logging.error(f"Error abriendo {input_pdf}: {e}")
        return False

    total_paginas = len(doc)
    log_msg(f"PDF abierto: {total_paginas} página(s).")
    
    # Soporte para modo test
    global total_paginas_override
    if 'total_paginas_override' in globals() and total_paginas_override:
        total_paginas = min(total_paginas, total_paginas_override)

    cola_tareas = queue.Queue(maxsize=BUFFER_IMAGENES)
    resultados_ocr = {}
    datos_render = {} 
    
    lock = threading.Lock()
    procesadas = [0]

    def worker_ocr():
        while True:
            item = cola_tareas.get()
            if item is None:
                cola_tareas.task_done()
                break
            
            idx, img_np = item
            for intento in range(1, REINTENTOS_PAGINA + 1):
                try:
                    result = reader.readtext(img_np)
                    with lock:
                        resultados_ocr[idx] = result
                        procesadas[0] += 1
                        print(
                            f"    [{procesadas[0]}/{total_paginas}] OCR página {idx+1} lista. (H:{threading.get_ident()})      ",
                            end="\r",
                            flush=True,
                        )
                    break
                except Exception as e:
                    if intento == REINTENTOS_PAGINA:
                        logging.error(f"Fallo OCR página {idx+1} en {input_pdf}: {e}")
                        with lock:
                            resultados_ocr[idx] = [] 
                            procesadas[0] += 1
                    time.sleep(1)
            
            cola_tareas.task_done()

    # Iniciar consumidores
    hilos = []
    for _ in range(MODO_TURBO_HILOS):
        t = threading.Thread(target=worker_ocr)
        t.start()
        hilos.append(t)
    log_msg(f"Hilos OCR activos: {MODO_TURBO_HILOS}. Renderizando páginas y encolando…")

    # Productor: Renderizado + Compresión (para que el PDF no pese 100MB)
    try:
        for i in range(total_paginas):
            for intento in range(1, REINTENTOS_PAGINA + 1):
                try:
                    log_msg(f"Render + compresión página {i + 1}/{total_paginas}…")
                    page = doc[i]
                    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
                    
                    # 1. Convertir Pixmap a PIL para comprimir (mismo motor que pdf_merger.py)
                    # Quitar transparencia (convertir a RGB con fondo blanco si es necesario)
                    if pix.n >= 4:
                        img_pil = Image.frombytes("RGBA", [pix.width, pix.height], pix.samples)
                        background = Image.new("RGB", img_pil.size, (255, 255, 255))
                        background.paste(img_pil, mask=img_pil.split()[3]) # 3 es el canal Alpha
                        img_pil = background
                    else:
                        img_pil = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

                    # 2. Reducir resolución si es necesario
                    if REDUCIR_RESOLUCION and img_pil.width > MAX_WIDTH:
                        ratio = MAX_WIDTH / float(img_pil.width)
                        new_height = int(float(img_pil.height) * float(ratio))
                        img_pil = img_pil.resize((MAX_WIDTH, new_height), Image.Resampling.LANCZOS)
                    
                    # 3. Guardar como JPEG comprimido
                    buffer_comp = io.BytesIO()
                    img_pil.save(buffer_comp, format="JPEG", quality=CALIDAD_JPEG, optimize=True)
                    img_jpeg_bytes = buffer_comp.getvalue()
                    
                    # Datos para OCR (usamos el numpy de la imagen ya convertida)
                    img_np = np.array(img_pil)
                    
                    datos_render[i] = {
                        'raw_img': img_jpeg_bytes,
                        'width': page.rect.width,
                        'height': page.rect.height,
                        # EasyOCR devuelve coords en esta imagen (puede estar reducida a MAX_WIDTH)
                        'ocr_w': img_pil.width,
                        'ocr_h': img_pil.height,
                    }
                    cola_tareas.put((i, img_np))
                    log_msg(f"Página {i + 1}/{total_paginas} en cola para OCR (EasyOCR puede tardar por página).")
                    break
                except Exception as e:
                    if intento == REINTENTOS_PAGINA:
                        logging.error(f"Error render página {i+1} en {input_pdf}: {e}")
                        cola_tareas.put((i, np.zeros((10,10,3), dtype=np.uint8)))
                    time.sleep(2)
    finally:
        doc.close()

    log_msg("Todas las páginas renderizadas. Esperando a que termine el OCR en cola…")
    cola_tareas.join()
    for _ in range(MODO_TURBO_HILOS):
        cola_tareas.put(None)
    for t in hilos:
        t.join()

    # Generación de PDF final (Searchable + Comprimido)
    log_msg("Generando PDF final (imagen + capa de texto invisible)…")
    try:
        new_doc = fitz.open()
        for i in range(total_paginas):
            p_data = datos_render.get(i)
            if not p_data: continue
            
            new_page = new_doc.new_page(width=p_data['width'], height=p_data['height'])
            
            # Insertar la imagen de fondo (ahora es un JPEG comprimido)
            new_page.insert_image(new_page.rect, stream=p_data['raw_img'])
            
            # Capa de texto invisible
            texto_pag = resultados_ocr.get(i, [])
            pw, ph = p_data['width'], p_data['height']
            ow = max(p_data.get('ocr_w') or 1, 1)
            oh = max(p_data.get('ocr_h') or 1, 1)
            scale_x = pw / ow
            scale_y = ph / oh
            for (bbox, text, prob) in texto_pag:
                if prob < 0.2: continue
                tl_raw = bbox[0]
                br_raw = bbox[2]
                x0 = float(tl_raw[0]) * scale_x
                y0 = float(tl_raw[1]) * scale_y
                x1 = float(br_raw[0]) * scale_x
                y1 = float(br_raw[1]) * scale_y
                rect_text = fitz.Rect(x0, y0, x1, y1)
                
                punto_insercion = fitz.Point(x0, y1) 
                try:
                    new_page.insert_text(
                        punto_insercion, 
                        text, 
                        fontname="helv", 
                        fontsize=rect_text.height * 0.9,
                        render_mode=3 
                    )
                except: pass
        
        new_doc.save(output_pdf, garbage=4, deflate=True, clean=True)
        new_doc.close()
        log_msg(f"Listo: {os.path.abspath(output_pdf)}")
        return True
    except Exception as e:
        log_msg(f"ERROR guardando PDF: {e}")
        logging.error(f"Error guardando {output_pdf}: {e}")
        return False

def _procesar_con_limite(p_pdf, p_reader, limit=None):
    global total_paginas_override
    total_paginas_override = limit
    return agregar_ocr_a_pdf(p_pdf, p_reader)


def _cargar_easyocr():
    """Una sola vez por proceso: import torch + modelos."""
    _boot_print("")
    _boot_print(">>> (1/2) import easyocr -> arrastra PyTorch; en cada proceso nuevo puede tardar mucho.")
    _boot_print(">>> (2/2) Reader() carga modelos en RAM (mas rapido si ya estan en cache).")
    log_msg(
        "Cargando EasyOCR (es+en). La primera vez: descarga modelos ~100MB. "
        "Por defecto el programa sigue vivo y puedes indicar mas PDFs despues."
    )
    t_imp = time.perf_counter()
    import easyocr  # noqa: E402

    log_msg(f"import easyocr terminado en {time.perf_counter() - t_imp:.1f} s.")
    t_rd = time.perf_counter()
    reader = easyocr.Reader(["es", "en"], gpu=False)
    log_msg(
        f"easyocr.Reader() listo en {time.perf_counter() - t_rd:.1f} s "
        f"(total arranque OCR {time.perf_counter() - t_imp:.1f} s)."
    )
    return reader


def _bucle_pedir_pdfs(reader, limite_test):
    """Pregunta rutas en bucle hasta vacío/q. Devuelve (exitos, fallos) de esta fase."""
    _boot_print("")
    _boot_print("EasyOCR ya esta en RAM. Escribe la ruta de un .pdf y Enter (o arrastra el archivo aqui).")
    _boot_print("  Linea vacia, q, quit o exit = terminar el programa.")
    ex = fa = 0
    while True:
        try:
            linea = input("PDF> ").strip()
        except (EOFError, KeyboardInterrupt):
            _boot_print("\nSaliendo.")
            break
        if not linea or linea.lower() in ("q", "quit", "exit"):
            break
        if (linea.startswith('"') and linea.endswith('"')) or (
            linea.startswith("'") and linea.endswith("'")
        ):
            linea = linea[1:-1]
        ruta = os.path.expanduser(linea)
        if not os.path.isfile(ruta):
            log_msg(f"No existe archivo: {ruta}")
            continue
        if not ruta.lower().endswith(".pdf"):
            log_msg("Tiene que ser un .pdf")
            continue
        if _procesar_con_limite(ruta, reader, limite_test):
            ex += 1
        else:
            fa += 1
    return ex, fa


if __name__ == "__main__":
    print("====================================================", flush=True)
    print("      BATCH TURBO OCR (MÁXIMA COMPRESIÓN)", flush=True)
    print("====================================================\n", flush=True)

    raw_args = sys.argv[1:]
    modo_batch = any(a == "--batch" for a in raw_args)
    modo_scan = any(a == "--scan" for a in raw_args)
    raw_args = [a for a in raw_args if a not in ("--batch", "--scan")]

    archivos_objetivo = []
    limite_test = None

    for arg in raw_args:
        if arg.lower() == "--test":
            limite_test = 4
            log_msg("MODO TEST: solo 4 páginas.")
        elif arg.lower() in ("--help", "-h"):
            _boot_print(
                "Uso: python ocr_converter.py [--batch] [--scan] [--test] [a.pdf b.pdf ...]\n"
                "  Por defecto: carga EasyOCR y luego pregunta que PDF quieres (una y otra vez).\n"
                "  Si pasas .pdf en la linea de comandos, los procesa primero y vuelve a preguntar.\n"
                "  --batch: solo procesa los PDF de la linea de comandos y sale (sin preguntar).\n"
                "  --scan: si no diste ningun .pdf, busca *_MASTER_COMPRESSED*.pdf en esta carpeta.\n"
                "  Varios .pdf en un comando: misma carga de EasyOCR para todos."
            )
            sys.exit(0)
        elif arg.lower().endswith(".pdf"):
            archivos_objetivo.append(arg)

    if not archivos_objetivo and modo_scan:
        archivos_objetivo = [
            f
            for f in os.listdir(".")
            if "_MASTER_COMPRESSED" in f and f.endswith(".pdf") and not f.endswith("_ocr.pdf")
        ]
        archivos_objetivo.sort()
        if archivos_objetivo:
            log_msg(f"--scan: en cola {len(archivos_objetivo)} PDF(s) *_MASTER_COMPRESSED*.")

    if modo_batch and not archivos_objetivo:
        log_msg("--batch sin ningun PDF: nada que hacer.")
        sys.exit(1)

    if archivos_objetivo:
        log_msg(f"En cola inicial: {', '.join(archivos_objetivo)}")
        if len(archivos_objetivo) > 1:
            log_msg("Varios PDF en un solo comando: EasyOCR se carga una vez para todos.")
    else:
        log_msg("Ningun PDF en la linea de comandos: se cargara EasyOCR y luego te preguntare.")

    reader = _cargar_easyocr()

    exitos = 0
    fallos = 0

    for archivo in archivos_objetivo:
        if _procesar_con_limite(archivo, reader, limite_test):
            exitos += 1
        else:
            fallos += 1

    if not modo_batch:
        e2, f2 = _bucle_pedir_pdfs(reader, limite_test)
        exitos += e2
        fallos += f2

    print(f"\n" + "="*50, flush=True)
    print(f"  RESUMEN: {exitos} exitosos, {fallos} fallidos.", flush=True)
    print("="*50, flush=True)
