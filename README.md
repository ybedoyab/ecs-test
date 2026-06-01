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
2. `python main.py` → `output/lab.pdf`, `lab_ocr.pdf`, `lab_small.pdf`.
3. `python claude.py` → `answers/lab.md` (bloques `<!-- TASK:t1_1 -->` …).
4. `python copy_task.py task1_1 regional_2526 --print` — con `--print` muestra pasos; sin flag solo portapapeles.
5. `python ask.py task1_1 ask.txt` → ayuda con error usando el bloque de esa tarea.

Prueba sin API: `python test_regional.py` y `python copy_task.py 1.1 regional_2526`.

PDF de ejemplo: `Regional_2526_Lab_ocr.pdf` en `Scripts/` (claude.py lo detecta solo).

## IDs de tarea

Acepta `task1_1`, `t1_1`, `1.1` → normaliza a `t1_1`.

## Formato markdown (generado por Claude)

Ver `prompts/claude_lab.md`. Cada tarea: `screenshots`, `copy` (fence), `files` (opcional).

Screenshots en consola: `screenshot 1-1-createuser`.

## Comandos

| Comando | Descripción |
|---------|-------------|
| `python main.py [nombre]` | Descarga + OCR + comprime |
| `python claude.py [nombre]` | Genera `answers/{nombre}.md` |
| `python copy_task.py task1_1 [lab]` | Copia solo el bloque de esa tarea |
| `python ask.py task1_1 ask.txt [lab]` | Pregunta sobre error en práctica |
| `copy t1_1` | Atajo Windows (`copy.cmd`) |
