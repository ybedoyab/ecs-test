# Huawei ICT — pipeline de práctica

## Setup

```bash
cd Scripts
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

`LAB_NAME` en `.env` es opcional; por defecto usa `lab`.

## Flujo

1. Pega el curl en `curl_comando.txt`.
2. `python main.py` → descarga + OCR + comprime.
3. `python main.py --claude openeuler regional_2526` → solo openEuler en el md (mantiene otras secciones).
4. `python claude.py regional_2526 opengauss` → solo openGauss (`g1_1`, …).
5. `python copy_task.py task1_1 regional_2526 --print` — pasos en pantalla; sin `--print` solo portapapeles.
6. `python ask.py task1_1 ask.txt` → ayuda con errores.

Prueba sin API: `python test_regional.py` y `python copy_task.py 1.1 regional_2526`.

PDF de ejemplo: `Regional_2526_Lab_ocr.pdf` en `Scripts/` (claude.py lo detecta solo).

## IDs de tarea

Acepta `task1_1`, `t1_1`, `1.1` → `t1_1` (openEuler). openGauss: `g1_1`. Kunpeng: `k1_1`.

## Formato markdown (generado por Claude)

Ver `prompts/claude_lab.md`. Cada tarea: `screenshots`, `copy` (fence), `files` (opcional).

Screenshots en consola: `screenshot 1-1-createuser`.

## Comandos

| Comando | Descripción |
|---------|-------------|
| `python main.py [nombre]` | Descarga + OCR + comprime |
| `python main.py --claude openeuler [lab]` | Claude solo sección openEuler |
| `python main.py --claude opengauss [lab]` | Claude solo openGauss (`g1_1`, …) |
| `python main.py --claude kunpeng [lab]` | Claude solo Kunpeng (`k1_1`, …) |
| `python claude.py [lab] [seccion]` | Igual que `--claude` sin descarga |
| `python copy_task.py task1_1 [lab]` | Copia solo el bloque de esa tarea |
| `python ask.py task1_1 ask.txt [lab]` | Pregunta sobre error en práctica |
| `copy t1_1` | Atajo Windows (`copy.cmd`) |
