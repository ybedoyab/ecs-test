import os
import sys
import fitz  # PyMuPDF
import io
from PIL import Image
from concurrent.futures import ThreadPoolExecutor

# ==========================================
# CONFIGURACIÓN DE COMPRESIÓN
# ==========================================
CALIDAD_JPEG = 75  # 1-100 (75 es el balance ideal)
REDUCIR_RESOLUCION = True 
MAX_WIDTH = 1280

def comprimir_una_imagen(img_data_tuple):
    """
    Función independiente para procesar una sola imagen en un hilo.
    """
    xref, width, height, samples, n = img_data_tuple
    try:
        # Convertir bytes a imagen PIL
        if n == 4: # RGBA
            img_pil = Image.frombytes("RGBA", [width, height], samples)
            img_pil = img_pil.convert("RGB") # Quitar transparencia para JPEG
        elif n == 3: # RGB
            img_pil = Image.frombytes("RGB", [width, height], samples)
        else: # Otros formatos (Grayscale, etc.)
            pix = fitz.Pixmap(fitz.csRGB, fitz.Pixmap(fitz.csRGB, width, height, samples, 0))
            img_pil = Image.frombytes("RGB", [width, height], pix.samples)

        # Reducir resolución si es muy grande
        if REDUCIR_RESOLUCION and img_pil.width > MAX_WIDTH:
            ratio = MAX_WIDTH / float(img_pil.width)
            new_height = int(float(img_pil.height) * float(ratio))
            img_pil = img_pil.resize((MAX_WIDTH, new_height), Image.Resampling.LANCZOS)
        
        # Guardar como JPEG en memoria
        buffer = io.BytesIO()
        img_pil.save(buffer, format="JPEG", quality=CALIDAD_JPEG, optimize=True)
        return xref, buffer.getvalue()
    except Exception as e:
        return xref, None

def optimizar_imagenes_del_doc(doc):
    """
    Recorre el documento PDF y comprime todas las imágenes pesadas de forma paralela.
    """
    print("    [*] Analizando y comprimiendo imágenes en paralelo...")
    
    # 1. Recolectar datos de todas las imágenes únicas
    xrefs_procesados = set()
    datos_para_procesar = []
    
    # Mapeo de xref a página para usar page.replace_image
    xref_to_page = {}

    for page_index in range(len(doc)):
        page = doc[page_index]
        # En PyMuPDF 1.27.x, el método es 'get_images'
        img_list = page.get_images()
        for img in img_list:
            xref = img[0]
            if xref in xrefs_procesados:
                continue
            xrefs_procesados.add(xref)
            xref_to_page[xref] = page_index
            
            try:
                # Extraer imagen y ver componentes (n)
                pix = fitz.Pixmap(doc, xref)
                datos_para_procesar.append((xref, pix.width, pix.height, pix.samples, pix.n))
            except:
                continue
    
    if not datos_para_procesar:
        print("    [*] No se detectaron imágenes optimizables.")
        return

    # 2. Procesar en paralelo
    print(f"    [*] Procesando {len(datos_para_procesar)} imágenes...")
    with ThreadPoolExecutor(max_workers=None) as executor:
        resultados = list(executor.map(comprimir_una_imagen, datos_para_procesar))
    
    # 3. Reinsertar los resultados en el PDF
    count = 0
    for xref, new_data in resultados:
        if new_data:
            try:
                page_idx = xref_to_page[xref]
                page = doc[page_idx]
                
                # Intentar reemplazo por Página (común en 1.18+)
                if hasattr(page, "replace_image"):
                    page.replace_image(xref, stream=new_data)
                # Intentar reemplazo por Documento
                elif hasattr(doc, "replace_image"):
                    doc.replace_image(xref, stream=new_data)
                else:
                    # Fallback manual robusto
                    doc.update_stream(xref, new_data)
                    doc.set_obj_value(xref, "Filter", fitz.PDF_NAME_DCTDECODE)
                    doc.set_obj_value(xref, "ColorSpace", fitz.PDF_NAME_DEVICERGB)
                count += 1
            except Exception as e:
                pass
            
    print(f"    [*] Se optimizaron {count} imágenes con éxito.")

def comprimir_archivo_individual(input_path):
    """
    Toma un solo archivo PDF (como uno procesado por OCR) y le aplica la compresión pesada.
    """
    if not os.path.exists(input_path):
        print(f"[!] El archivo no existe: {input_path}")
        return
    
    output_path = input_path.replace(".pdf", "_small.pdf")
    print(f"\n[*] Optimizando archivo individual: {input_path}")
    
    doc = fitz.open(input_path)
    size_original = os.path.getsize(input_path)
    
    # Aplicar la misma optimización que el merger
    optimizar_imagenes_del_doc(doc)
    
    print(f"[*] Guardando versión comprimida: {output_path}")
    doc.save(output_path, garbage=4, deflate=True, clean=True)
    doc.close()
    
    size_final = os.path.getsize(output_path)
    ahorro = (1 - (size_final / size_original)) * 100
    print(f"[!] ¡LISTO!")
    print(f"    - Tamaño original: {size_original / (1024*1024):.2f} MB")
    print(f"    - Tamaño optimizado: {size_final / (1024*1024):.2f} MB")
    print(f"    - REDUCCIÓN: {ahorro:.1f}%")

def merge_and_compress_pdfs():
    print("====================================================")
    print("      SÚPER PDF TOOL: MERGER & COMPRESSOR PRO")
    print("====================================================\n")
    
    # 0. Verificar si es modo compresión individual
    args = [a.lower() for a in sys.argv]
    if "--compress" in args:
        idx = args.index("--compress")
        if idx + 1 < len(sys.argv):
            target = sys.argv[idx + 1]
            comprimir_archivo_individual(target)
            return
        else:
            print("[!] Uso: python pdf_merger.py --compress mi_archivo.pdf")
            return

    # 1. Obtener todos los PDFs pero ignorar los ya mergeados u OCR
    todos_los_pdfs = [f for f in os.listdir('.') 
                      if f.lower().endswith('.pdf') 
                      and '_merged' not in f.lower().replace('full_merged', '')
                      and 'master' not in f.lower()
                      and '_ocr' not in f.lower()]
    
    if not todos_los_pdfs:
        print("[!] No se encontraron archivos PDF para unir.")
        return

    # 2. Agrupar por prefijo
    grupos = {}
    for f in todos_los_pdfs:
        prefix = f.split('_')[0]
        if prefix not in grupos:
            grupos[prefix] = []
        grupos[prefix].append(f)
    
    # 3. Filtrar por argumento si existe
    filtro = None
    for arg in sys.argv:
        if arg.startswith('--') and arg != '--compress':
            filtro = arg[2:].upper()
            break
    
    if filtro:
        if filtro in grupos:
            grupos = {filtro: grupos[filtro]}
            print(f"[*] Filtrando solo para el prefijo: {filtro}")
        else:
            print(f"[!] El prefijo '{filtro}' no fue encontrado.")
            return
    
    # 4. Procesar cada grupo
    for prefix, archivos in grupos.items():
        if len(archivos) < 1: continue
        archivos.sort()
        output_filename = f"{prefix}_MASTER_COMPRESSED.pdf"
        
        print(f"\n[*] Creando MASTER para '{prefix}' ({len(archivos)} archivos)...")
        doc_maestro = fitz.open()
        size_original_total = 0
        
        for pdf in archivos:
            print(f"    - Uniendo: {pdf}")
            size_original_total += os.path.getsize(pdf)
            with fitz.open(pdf) as d:
                doc_maestro.insert_pdf(d)
        
        # APLICAR COMPRESIÓN DE IMÁGENES
        optimizar_imagenes_del_doc(doc_maestro)
        
        # GUARDAR
        print(f"[*] Guardando archivo maestro final: {output_filename}")
        doc_maestro.save(output_filename, garbage=4, deflate=True, clean=True)
        doc_maestro.close()
        
        size_final = os.path.getsize(output_filename)
        ahorro = (1 - (size_final / size_original_total)) * 100
        print(f"[!] ¡TERMINADO!")
        print(f"    - Peso original sumado: {size_original_total / (1024*1024):.2f} MB")
        print(f"    - Peso final optimizado: {size_final / (1024*1024):.2f} MB")
        print(f"    - AHORRO DE ESPACIO: {ahorro:.1f}%")

if __name__ == "__main__":
    try:
        merge_and_compress_pdfs()
    except Exception as e:
        print(f"\n[!] Error: {e}")
