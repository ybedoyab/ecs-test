import base64
import json
import ssl
import threading
import time
from pathlib import Path

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

API_URL = "https://api.anthropic.com/v1/messages"
MODEL = "claude-sonnet-4-6"
LOG = "[help]"
PROFILE_VER = "4.6"
EFFORT_LAB = "medium"
EFFORT_CHAT = "low"
HEALTH_EVERY = 15
MAX_RETRIES = 5
BACKOFF_BASE = 2

_SESSION: requests.Session | None = None
_TRANSIENT = (
    requests.exceptions.SSLError,
    requests.exceptions.ConnectionError,
    requests.exceptions.ChunkedEncodingError,
    requests.exceptions.ReadTimeout,
)


def _ssl_context() -> ssl.SSLContext:
    ctx = ssl.create_default_context()
    if hasattr(ssl, "OP_IGNORE_UNEXPECTED_EOF"):
        ctx.options |= ssl.OP_IGNORE_UNEXPECTED_EOF
    return ctx


class _SSLAdapter(HTTPAdapter):
    """Pasa ssl_context al pool; requests 2.34+ no acepta SSLContext en verify=."""

    def __init__(self, ssl_context: ssl.SSLContext | None = None, **kwargs):
        self._ssl_context = ssl_context
        super().__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False, **pool_kwargs):
        if self._ssl_context is not None:
            pool_kwargs["ssl_context"] = self._ssl_context
        return super().init_poolmanager(connections, maxsize, block=block, **pool_kwargs)


def _session() -> requests.Session:
    global _SESSION
    if _SESSION is not None:
        return _SESSION
    retry = Retry(
        total=3,
        connect=3,
        read=3,
        backoff_factor=1,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset(["POST"]),
        raise_on_status=False,
    )
    adapter = _SSLAdapter(
        ssl_context=_ssl_context(),
        max_retries=retry,
        pool_connections=4,
        pool_maxsize=4,
    )
    s = requests.Session()
    s.mount("https://", adapter)
    _SESSION = s
    return s


def _headers(api_key: str) -> dict:
    return {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
        "accept": "text/event-stream",
        "connection": "keep-alive",
    }


def _apply_profile(body: dict, effort: str, *, thinking: bool = True) -> dict:
    out = dict(body)
    if thinking:
        out["thinking"] = {"type": "adaptive"}
    out["output_config"] = {"effort": effort}
    return out


def _profile_tag(effort: str) -> str:
    return f"{PROFILE_VER} {effort}"


def _is_transient(exc: BaseException) -> bool:
    if isinstance(exc, _TRANSIENT):
        return True
    msg = str(exc).lower()
    return "unexpected_eof" in msg or "eof occurred" in msg


def _heartbeat(stop: threading.Event, label: str, start: float) -> None:
    while not stop.wait(HEALTH_EVERY):
        sec = int(time.time() - start)
        print(f"\n{LOG} {label} activo ({sec}s)", flush=True)


def _consume_sse(buffer: str, parts: list[str], show: bool, state: dict) -> str:
    current_event = None
    while "\n" in buffer:
        line, buffer = buffer.split("\n", 1)
        line = line.strip()
        if line.startswith("event:"):
            current_event = line[6:].strip()
            if show and current_event == "ping":
                print(f"\n{LOG} ok", flush=True)
            continue
        if not line.startswith("data:"):
            continue
        payload = line[5:].strip()
        if not payload or payload == "[DONE]":
            continue
        try:
            event = json.loads(payload)
        except json.JSONDecodeError:
            continue
        etype = event.get("type") or current_event

        if etype == "message_start":
            continue

        if etype == "content_block_start":
            block = event.get("content_block") or {}
            btype = block.get("type")
            state["block"] = btype
            if btype == "thinking":
                state["thinking_started"] = True
            elif btype == "text" and show:
                if state.get("thinking_started"):
                    print()
                state["text_started"] = True
            continue

        if etype == "content_block_delta":
            delta = event.get("delta") or {}
            dtype = delta.get("type")
            if dtype == "thinking_delta":
                pass
            elif dtype == "signature_delta":
                pass
            elif dtype == "text_delta":
                text = delta.get("text") or ""
                if text:
                    parts.append(text)
                    if show:
                        print(text, end="", flush=True)
            continue

        if etype == "content_block_stop":
            state["block"] = None
            continue

        if etype == "message_delta":
            continue

        if etype == "error":
            raise RuntimeError(event.get("error", event))

    return buffer


def _read_stream(resp: requests.Response, parts: list[str], show: bool, state: dict) -> None:
    buffer = ""
    for chunk in resp.iter_content(chunk_size=4096, decode_unicode=False):
        if not chunk:
            continue
        buffer += chunk.decode("utf-8", errors="replace")
        buffer = _consume_sse(buffer, parts, show, state)
    if buffer.strip():
        _consume_sse(buffer + "\n", parts, show, state)


def _post_stream(
    api_key: str,
    body: dict,
    *,
    label: str = "lab",
    effort: str = EFFORT_LAB,
    show: bool = True,
    thinking: bool = True,
) -> str:
    body = _apply_profile(body, effort, thinking=thinking)
    body = {**body, "stream": True}
    payload = json.dumps(body)
    upload_mb = len(payload) / (1024 * 1024)
    connect_timeout = max(60, int(upload_mb * 10))
    if show:
        print(f"{LOG} {_profile_tag(effort)} — generando...", flush=True)
        if upload_mb > 1:
            print(f"{LOG} envio ~{upload_mb:.1f} MB, espera {connect_timeout}s", flush=True)

    start = time.time()
    stop = threading.Event()
    threading.Thread(target=_heartbeat, args=(stop, label, start), daemon=True).start()
    parts: list[str] = []
    state: dict = {"block": None, "thinking_started": False, "text_started": False}
    last_err: BaseException | None = None

    try:
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                resp = _session().post(
                    API_URL,
                    data=payload,
                    headers=_headers(api_key),
                    stream=True,
                    timeout=(connect_timeout, 600),
                )
                if resp.status_code >= 400:
                    err_body = resp.text
                    resp.close()
                    raise RuntimeError(f"HTTP {resp.status_code}: {err_body}")
                if show:
                    print(f"{LOG} conectado\n", flush=True)
                _read_stream(resp, parts, show, state)
                resp.close()
                last_err = None
                break
            except _TRANSIENT as e:
                last_err = e
            except requests.exceptions.RequestException as e:
                if _is_transient(e):
                    last_err = e
                else:
                    raise RuntimeError(str(e)) from e
            if last_err is None:
                break
            if attempt >= MAX_RETRIES:
                break
            wait = BACKOFF_BASE ** (attempt - 1)
            if show:
                print(
                    f"\n{LOG} red inestable, reintento {attempt}/{MAX_RETRIES} en {wait}s...",
                    flush=True,
                )
            time.sleep(wait)
            parts.clear()
            state = {"block": None, "thinking_started": False, "text_started": False}
    finally:
        stop.set()

    if last_err is not None:
        raise RuntimeError(f"Conexion SSL/red fallo tras {MAX_RETRIES} intentos: {last_err}") from last_err

    if show:
        print(
            f"\n{LOG} {label} listo ({int(time.time() - start)}s)\n",
            flush=True,
        )
    return "".join(parts).strip()


def _post_sync(api_key: str, body: dict, *, effort: str = EFFORT_LAB, thinking: bool = True) -> str:
    body = _apply_profile(body, effort, thinking=thinking)
    payload = json.dumps(body)
    last_err: BaseException | None = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = _session().post(
                API_URL,
                data=payload,
                headers={k: v for k, v in _headers(api_key).items() if k != "accept"},
                timeout=(60, 600),
            )
            if resp.status_code >= 400:
                raise RuntimeError(f"HTTP {resp.status_code}: {resp.text}")
            data = resp.json()
            texts = []
            for block in data.get("content") or []:
                if block.get("type") == "text":
                    texts.append(block.get("text") or "")
            return "\n".join(texts).strip()
        except _TRANSIENT as e:
            last_err = e
        except requests.exceptions.RequestException as e:
            if _is_transient(e):
                last_err = e
            else:
                raise RuntimeError(str(e)) from e
        if attempt < MAX_RETRIES:
            time.sleep(BACKOFF_BASE ** (attempt - 1))
    raise RuntimeError(f"Conexion SSL/red fallo tras {MAX_RETRIES} intentos: {last_err}") from last_err


def text(
    api_key: str,
    system: str,
    user: str,
    max_tokens: int = 4096,
    stream: bool = True,
    *,
    thinking: bool = False,
) -> str:
    body = {
        "model": MODEL,
        "max_tokens": max_tokens,
        "system": system,
        "messages": [{"role": "user", "content": user}],
    }
    if stream:
        return _post_stream(
            api_key, body, label="texto", effort=EFFORT_LAB, thinking=thinking
        )
    return _post_sync(api_key, body, effort=EFFORT_LAB, thinking=thinking)


def chat(api_key: str, system: str, messages: list[dict], max_tokens: int = 4096, stream: bool = True) -> str:
    body = {
        "model": MODEL,
        "max_tokens": max_tokens,
        "system": system,
        "messages": messages,
    }
    if stream:
        return _post_stream(api_key, body, label="chat", effort=EFFORT_CHAT)
    return _post_sync(api_key, body, effort=EFFORT_CHAT)


def pdf_markdown(api_key: str, system: str, pdf_path: Path, stream: bool = True) -> str:
    """Legacy: sube el PDF en base64 (lento). Usar claude_run + pdf_text + text()."""
    if stream:
        print(f"{LOG} leyendo {pdf_path.name}...", flush=True)
    raw = pdf_path.read_bytes()
    b64 = base64.standard_b64encode(raw).decode("ascii")
    if stream:
        mb = len(raw) / (1024 * 1024)
        print(f"{LOG} {_profile_tag(EFFORT_LAB)} — enviando ({mb:.1f} MB)...", flush=True)
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
    label = f"pdf:{pdf_path.name}"
    if stream:
        return _post_stream(api_key, body, label=label, effort=EFFORT_LAB)
    return _post_sync(api_key, body, effort=EFFORT_LAB)
