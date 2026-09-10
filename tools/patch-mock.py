import re
p = r"D:\合曜AI\golden-flower-ei\tools\mock-llm.py"
data = open(p, "rb").read().decode("utf-8")

# Find the streaming loop and replace the per-line loop with a single chunk
old = """            for line in reply.split(chr(10)):
                chunk["choices"][0]["delta"] = {"content": line + chr(10)}
                sse = "data: " + json.dumps(chunk, ensure_ascii=False) + chr(10) + chr(10)
                self.wfile.write(sse.encode("utf-8"))
                self.wfile.flush()
            chunk["choices"][0]["delta"] = {}
            chunk["choices"][0]["finish_reason"] = "stop"
            sse = "data: " + json.dumps(chunk, ensure_ascii=False) + chr(10) + chr(10)
            self.wfile.write(sse.encode("utf-8"))
            self.wfile.write(b"data: [DONE]" + (chr(10) * 2).encode("utf-8"))
            self.wfile.flush()"""
new = """            # Send the full content in ONE chunk (client is impatient)
            chunk["choices"][0]["delta"] = {"content": reply}
            sse = "data: " + json.dumps(chunk, ensure_ascii=False) + chr(10) + chr(10)
            self.wfile.write(sse.encode("utf-8"))
            self.wfile.flush()
            chunk["choices"][0]["delta"] = {}
            chunk["choices"][0]["finish_reason"] = "stop"
            sse = "data: " + json.dumps(chunk, ensure_ascii=False) + chr(10) + chr(10)
            self.wfile.write(sse.encode("utf-8"))
            self.wfile.flush()
            self.wfile.write(b"data: [DONE]" + (chr(10) * 2).encode("utf-8"))
            self.wfile.flush()"""
patched = data.replace(old, new)
with open(p, "wb") as f:
    f.write(patched.encode("utf-8"))
print("OK" if patched != data else "no change")
