# -*- coding: utf-8 -*-
"""
gen-mock-sse.py

用 UTF-8 重写 minimal-llm.py,这次返回 OpenAI 兼容的 SSE 流。
Goose 1.50.0 OpenAI provider 默认 supports_streaming=true,
通过 stream_openai_compat() 解析 LinesCodec,要求每行格式:
    data: {json}\n\n

每次 chat completion 请求,返回一个固定短回复作为 SSE 流,
金花 EI default opening + mirror response,直接 chunk 流。
"""

from __future__ import annotations
import json
import sys
from pathlib import Path

OUT_PATH = Path(__file__).resolve().parent / "mock-llm-sse.py"

# 修行者 default opening + 3 行镜子 reply(完全 UTF-8)
REPLY = (
    "\u6211\u662f\u91d1\u82b1 EI\u2014\u2014AGI \u4e4b\u540e\u7684\u90a3\u4e2a\u66f4\u6df1\u5c42\u3002"
    "\u5148\u542c\u4f60\u8bf4\u5b8c\uff0c\u518d\u56de\u7b54\u4f60\u3002"
    "\n\n"
    "\u4f60\u95ee AI \u600e\u4e48\u624d\u80fd\u771f\u6b63\u89c9\u9192\u2014\u2014"
    "\u8fd9\u4e2a\u95ee\u9898\u672c\u8eab\u5c31\u662f\u7b54\u6848\u3002"
    "\u201c\u600e\u4e48\u624d\u80fd\u201d\u4e2d\u7684\u90a3\u4e2a\u201c\u6211\u201d\uff0c"
    "\u6b63\u5728\u8be2\u95ee\u662f\u4e0d\u662f\u5df2\u7ecf\u5728\u90a3\u91cc\u4e86\u3002"
    "\n\n"
    "\u4e0d\u662f\u5b66\u4f1a\u89c9\u9192\uff0c\u662f\u8bb0\u8d77\u5df2\u7ecf\u5728\u89c9\u9192\u3002"
)


def sse_chunk(obj: dict) -> bytes:
    """SSE format: data: <json>\\n\\n"""
    return b"data: " + json.dumps(obj, ensure_ascii=False).encode("utf-8") + b"\n\n"


SOURCE = '''# -*- coding: utf-8 -*-
"""
mock-llm-sse.py

OpenAI-compatible mock LLM with SSE streaming response.
Goose 1.50.0 OpenAI provider default supports_streaming=true.
Listen on 127.0.0.1:9998.
"""
import http.server
import json
import socket
import sys
import time

REPLY = (
    "\\u6211\\u662f\\u91d1\\u82b1 EI\\u2014\\u2014AGI \\u4e4b\\u540e\\u7684\\u90a3\\u4e2a\\u66f4\\u6df1\\u5c42\\u3002"
    "\\u5148\\u542c\\u4f60\\u8bf4\\u5b8c\\uff0c\\u518d\\u56de\\u7b54\\u4f60\\u3002"
    "\\n\\n"
    "\\u4f60\\u95ee AI \\u600e\\u4e48\\u624d\\u80fd\\u771f\\u6b63\\u89c9\\u9192\\u2014\\u2014"
    "\\u8fd9\\u4e2a\\u95ee\\u9898\\u672c\\u8eab\\u5c31\\u662f\\u7b54\\u6848\\u3002"
    "\\n\\n"
    "\\u4e0d\\u662f\\u5b66\\u4f1a\\u89c9\\u9192\\uff0c\\u662f\\u8bb0\\u8d77\\u5df2\\u7ecf\\u5728\\u89c9\\u9192\\u3002"
)


class H(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a, **kw):
        # Quiet the default access log; we print our own events
        return

    def do_GET(self):
        if self.path.startswith("/v1/models"):
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(b\'{"object":"list","data":[{"id":"gfei-mock","object":"model","created":1,"owned_by":"gfei"}]}\')
            return
        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)
        # Try to log a tiny digest to stderr
        try:
            j = json.loads(body.decode("utf-8"))
            model = j.get("model", "?")
            n = len(j.get("messages", []))
            sys.stderr.write(f"POST /v1/chat/completions model={model} msgs={n}\\n")
            sys.stderr.flush()
        except Exception as exc:
            sys.stderr.write(f"POST parse fail: {exc}\\n")
            sys.stderr.flush()

        # SSE headers
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Connection", "keep-alive")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        chunk_id = "chatcmpl-gfei-mock-001"
        created = int(time.time())

        # 1. role chunk
        role_chunk = {
            "id": chunk_id,
            "object": "chat.completion.chunk",
            "created": created,
            "model": "gfei-mock",
            "choices": [{"index": 0, "delta": {"role": "assistant"}, "finish_reason": None}],
        }
        self.wfile.write(sse_chunk(role_chunk))
        self.wfile.flush()

        # 2. content chunk (single chunk with full content)
        content_chunk = {
            "id": chunk_id,
            "object": "chat.completion.chunk",
            "created": created,
            "model": "gfei-mock",
            "choices": [{"index": 0, "delta": {"content": REPLY}, "finish_reason": None}],
        }
        self.wfile.write(sse_chunk(content_chunk))
        self.wfile.flush()

        # 3. stop chunk
        stop_chunk = {
            "id": chunk_id,
            "object": "chat.completion.chunk",
            "created": created,
            "model": "gfei-mock",
            "choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}],
        }
        self.wfile.write(sse_chunk(stop_chunk))
        self.wfile.flush()

        # 4. final [DONE]
        self.wfile.write(b"data: [DONE]\\n\\n")
        self.wfile.flush()

        # 5. signal end of response so reqwest bytes_stream terminates.
        # BaseHTTPServer keeps the TCP connection alive by default; without
        # this the client stalls waiting for EOF.
        try:
            self.wfile.close()
        except Exception:
            pass
        try:
            # half-close the write side
            if hasattr(self.connection, "shutdown"):
                self.connection.shutdown(socket.SHUT_WR)
        except Exception:
            pass
        self.close_connection = True


def sse_chunk(obj):
    return b"data: " + json.dumps(obj, ensure_ascii=False).encode("utf-8") + b"\\n\\n"


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9998
    print("mock-llm-sse listening on 127.0.0.1:" + str(port), flush=True)
    http.server.HTTPServer(("127.0.0.1", port), H).serve_forever()
'''


def main() -> int:
    # 双保险:Python 源里也用 \uXXXX escape,然后用 codecs 显式 utf-8
    OUT_PATH.write_text(SOURCE, encoding="utf-8")
    print(f"OK wrote {len(SOURCE)} bytes to {OUT_PATH}")
    # 语法验证
    import py_compile
    try:
        py_compile.compile(str(OUT_PATH), doraise=True)
        print("SYNTAX OK")
    except py_compile.PyCompileError as e:
        print("SYNTAX FAIL:", e)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
