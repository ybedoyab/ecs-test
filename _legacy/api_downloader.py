import os
import time
import sys
import re
import urllib.request
import urllib.parse
import ssl
from PIL import Image

# ==========================================
# CONFIGURACIÓN
# ==========================================
DEFAULT_TOTAL_SLIDES = 1
OUTPUT_PDF = "Global_2425_Lab.pdf"
CARPETA_DESTINO = "."
ARCHIVO_CURL = "curl_comando.txt"

def clean_windows_escapes(text):
    """
    Limpia de forma agresiva los escapes de Windows CMD (^).
    """
    # 1. Quitar continuaciones de línea (^\n o ^\r\n)
    text = re.sub(r'\^[\r\n]+', '', text)
    
    # 2. Limpiar escapes de caracteres especiales (^" -> ", ^& -> &, etc.)
    text = re.sub(r'\^([\s\S])', r'\1', text)
    
    return text

def parse_curl_to_request(curl_str):
    # 1. Limpieza inicial profunda de carets ^
    clean = clean_windows_escapes(curl_str)
    
    # 2. Extraer URL
    url_match = re.search(r'(https?://[^\s"\'\^]+)', clean)
    url = url_match.group(1) if url_match else None
    if url:
        url = url.strip().strip('"').strip("'")

    # 3. Extraer Headers
    headers = {}
    header_matches = re.finditer(r'-H\s+["\']([^:]+):\s*(.*?)["\']', clean)
    for match in header_matches:
        key = match.group(1).strip()
        value = match.group(2).strip()
        headers[key] = value

    # 4. Extraer Cookies
    cookie_match = re.search(r'-b\s+["\'](.*?)["\']', clean)
    if cookie_match:
        headers['Cookie'] = cookie_match.group(1)

    # 5. Extraer Data Raw (Payload JSON)
    data = None
    json_match = re.search(r'(\{.*\})', clean, re.DOTALL)
    if json_match:
        data = json_match.group(1).strip()
        # IMPORTANTE: Quitar los backslashes de escape que pone Windows (\")
        data = data.replace('\\"', '"')
    
    method = 'POST' if data else 'GET'
    
    # Especial para PUT si está el flag -X
    method_match = re.search(r'-X\s+["\']?([A-Z]+)["\']?', clean)
    if method_match:
        method = method_match.group(1)

    return url, headers, data, method

def descargar_imagenes(full_curl):
    url, headers, raw_data_template, base_method = parse_curl_to_request(full_curl)
    
    if not url:
        print("[!] Error fatal: No se pudo identificar la URL en el comando cURL.")
        sys.exit(1)
        
    print(f"[*] URL detectada: {url[:70]}...")
    print(f"[*] Método: {base_method}")
    print(f"[*] Headers detectados: {len(headers)}")
    
    # Detectar total de páginas desde el JSON
    total_slides = DEFAULT_TOTAL_SLIDES
    if raw_data_template:
        match_total = re.search(r'"totalPage"\s*:\s*(\d+)', raw_data_template)
        if match_total:
            total_slides = int(match_total.group(1))
            print(f"[*] Total de páginas detectadas: {total_slides}")
        else:
            print(f"[*] Usando valor por defecto de páginas: {total_slides}")
            
    # Contexto SSL para ignorar errores de certificado
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    from concurrent.futures import ThreadPoolExecutor
    import threading

    print(f"\nIniciando descarga de {total_slides} diapositivas (Modo Turbo)...")
    
    lock = threading.Lock()
    contador = [0]
    
    def descargar_una_pagina(page):
        filename = os.path.join(CARPETA_DESTINO, f"slide_{page:03d}.png")
        
        if os.path.exists(filename) and os.path.getsize(filename) > 1000:
            with lock:
                contador[0] += 1
                print(f"  [{contador[0]}/{total_slides}] Ya existe. Saltando.", end="\r")
            return
            
        # Preparar payload
        payload_bytes = None
        if raw_data_template:
            current_payload = re.sub(
                r'("pageNum"\s*:\s*)\d+',
                lambda m: f'{m.group(1)}{page}',
                raw_data_template
            )
            payload_bytes = current_payload.encode('utf-8')
            
        req = urllib.request.Request(url, data=payload_bytes, headers=headers, method=base_method)
        
        for intento in range(1, 4):
            try:
                with urllib.request.urlopen(req, context=ctx, timeout=30) as response:
                    content = response.read()
                    
                with open(filename, 'wb') as f:
                    f.write(content)
                
                if os.path.getsize(filename) < 1000:
                    os.remove(filename)
                    return # Fallo crítico, no reintentos aquí
                
                with lock:
                    contador[0] += 1
                    print(f"  [{contador[0]}/{total_slides}] Descargado con éxito.        ", end="\r")
                return
                
            except Exception as e:
                if intento == 3:
                    print(f"\n[!] Error persistente en página {page}: {e}")
                time.sleep(1)

    # Lanzar descargas en paralelo (10 hilos)
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(descargar_una_pagina, range(1, total_slides + 1))

    print(f"\n\n¡Download completo! {total_slides} diapositivas listas.")
    return total_slides

def crear_pdf(num_imagenes):
    print(f"Convirtiendo a {OUTPUT_PDF}...")
    
    archivos = sorted([f for f in os.listdir(CARPETA_DESTINO) if f.startswith('slide_') and f.endswith('.png')])
    
    if not archivos:
        print("[!] No hay imágenes para convertir.")
        return
        
    print(f"Procesando {len(archivos)} imágenes...")
    imagenes = []
    for f in archivos:
        path = os.path.join(CARPETA_DESTINO, f)
        img = Image.open(path).convert('RGB')
        imagenes.append(img)
        
    if imagenes:
        output_path = os.path.join(CARPETA_DESTINO, OUTPUT_PDF)
        imagenes[0].save(output_path, save_all=True, append_images=imagenes[1:])
        print(f"[*] PDF creado satisfactoriamente en: {output_path}")
        
        print("[*] Limpiando archivos temporales...")
        for f in archivos:
            try:
                os.remove(os.path.join(CARPETA_DESTINO, f))
            except:
                pass
    
if __name__ == "__main__":
    print("====================================================")
    print("  HUAWEI ACADEMY PDF DOWNLOADER (OPTIMIZADO)")
    print("====================================================\n")
    
    if not os.path.exists(ARCHIVO_CURL):
        print(f"[!] No se encontró '{ARCHIVO_CURL}'")
        with open(ARCHIVO_CURL, "w", encoding="utf-8") as f:
            f.write("# PEGA EL CURL AQUÍ\n")
        exit(0)
        
    with open(ARCHIVO_CURL, "r", encoding="utf-8") as f:
        full_curl = f.read()
    
    if "curl" not in full_curl.lower():
        print("[!] El archivo no contiene un comando cURL válido.")
        exit(1)
        
    num = descargar_imagenes(full_curl)
    crear_pdf(num)
