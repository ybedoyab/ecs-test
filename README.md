# Huawei ICT — pipeline de práctica

## Setup

```bash
cd Scripts
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

## Flujo

```bash
python main.py
```

1. Verifica `context/` (openeuler, opengauss, kunpeng)
2. Pregunta si continuar con descarga del lab (curl → PDF → OCR)

Chats (sin re-entrenar):

```bash
python ask.py openeuler
python ask.py opengauss
python ask.py kunpeng
```

## context/

Conocimiento pre-entrenado en `context/{seccion}/knowledge.md`. Va en el repo; no hay carpeta `material/`.

## Otros

| Comando | Descripción |
|---------|-------------|
| `python claude.py regional_2526 openeuler` | Genera answers del lab PDF |
| `python copy_task.py 1.1 regional_2526 --print` | Copia tarea |
| `copy t1_1` | Atajo Windows |
