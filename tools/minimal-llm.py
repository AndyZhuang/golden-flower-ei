import http.server
import json
import sys

class H(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a, **kw):
        print("LOG:", self.path, self.command, file=sys.stderr, flush=True)

    def do_GET(self):
        print("GET HIT", self.path, flush=True)
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"object":"list","data":[{"id":"gfei-mock"}]}')

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)
        print("POST HIT", self.path, "body-bytes", len(body), flush=True)
        print("  body[:300]:", body[:300], flush=True)
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        # Non-stream single response with full content
        payload = {
            "id": "x",
            "object": "chat.completion",
            "created": 1,
            "model": "gfei-mock",
            "choices": [
                {
                    "index": 0,
                    "message": {"role": "assistant", "content": "hi from minimal"},
                    "finish_reason": "stop",
                }
            ],
            "usage": {},
        }
        data = json.dumps(payload).encode("utf-8")
        self.wfile.write(data)
        self.wfile.flush()
        print("POST DONE", flush=True)


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9998
    print("listening on 127.0.0.1:" + str(port), flush=True)
    http.server.HTTPServer(("127.0.0.1", port), H).serve_forever()
