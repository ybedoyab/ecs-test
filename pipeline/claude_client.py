import base64
import json
import urllib.request
from pathlib import Path

API_URL = "https://api.anthropic.com/v1/messages"
MODEL = "claude-sonnet-4-20250514"


def _post(api_key: str, body: dict) -> str:
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=300) as resp:
        data = json.loads(resp.read().decode())
    parts = []
    for block in data.get("content", []):
        if block.get("type") == "text":
            parts.append(block.get("text", ""))
    return "\n".join(parts).strip()


def text(api_key: str, system: str, user: str, max_tokens: int = 4096) -> str:
    body = {
        "model": MODEL,
        "max_tokens": max_tokens,
        "system": system,
        "messages": [{"role": "user", "content": user}],
    }
    return _post(api_key, body)


def chat(api_key: str, system: str, messages: list[dict], max_tokens: int = 4096) -> str:
    body = {
        "model": MODEL,
        "max_tokens": max_tokens,
        "system": system,
        "messages": messages,
    }
    return _post(api_key, body)


def pdf_markdown(api_key: str, system: str, pdf_path: Path) -> str:
    raw = pdf_path.read_bytes()
    b64 = base64.standard_b64encode(raw).decode("ascii")
    body = {
        "model": MODEL,
        "max_tokens": 16384,
        "system": system,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "document",
                        "source": {
                            "type": "base64",
                            "media_type": "application/pdf",
                            "data": b64,
                        },
                    },
                    {
                        "type": "text",
                        "text": "Genera el markdown de todas las tareas del lab siguiendo el formato indicado en system.",
                    },
                ],
            }
        ],
    }
    return _post(api_key, body)
