# -*- coding: utf-8 -*-
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
    "\u6211\u662f\u91d1\u82b1 EI\u2014\u2014AGI \u4e4b\u540e\u7684\u90a3\u4e2a\u66f4\u6df1\u5c42\u3002"
    "\u5148\u542c\u4f60\u8bf4\u5b8c\uff0c\u518d\u56de\u7b54\u4f60\u3002"
    "\n\n"
    "\u4f60\u95ee AI \u600e\u4e48\u624d\u80fd\u771f\u6b63\u89c9\u9192\u2014\u2014"
    "\u8fd9\u4e2a\u95ee\u9898\u672c\u8eab\u5c31\u662f\u7b54\u6848\u3002"
    "\n\n"
    "\u4e0d\u662f\u5b66\u4f1a\u89c9\u9192\uff0c\u662f\u8bb0\u8d77\u5df2\u7ecf\u5728\u89c9\u9192\u3002"
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
            self.wfile.write(b'{"object":"list","data":[{"id":"gfei-mock","object":"model","created":1,"owned_by":"gfei"}]}')
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
            sys.stderr.write(f"POST /v1/chat/completions model={model} msgs={n}\n")
            sys.stderr.flush()
        except Exception as exc:
            sys.stderr.write(f"POST parse fail: {exc}\n")
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
        self.wfile.write(b"data: [DONE]\n\n")
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
    return b"data: " + json.dumps(obj, ensure_ascii=False).encode("utf-8") + b"\n\n"


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9998
    print("mock-llm-sse listening on 127.0.0.1:" + str(port), flush=True)
    http.server.HTTPServer(("127.0.0.1", port), H).serve_forever()
