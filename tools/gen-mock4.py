"""Patch mock-llm.py to remove the per-chunk sleep (cause of client abort)."""
import re

p = r"D:\合曜AI\golden-flower-ei\tools\mock-llm.py"
data = open(p, "rb").read().decode("utf-8")
# Remove the time.sleep(0.02) line and its surrounding empty line context
patched = re.sub(
    r"                self\.wfile\.flush\(\)\n                time\.sleep\(0\.02\)\n",
    "                self.wfile.flush()\n",
    data,
)
with open(p, "wb") as f:
    f.write(patched.encode("utf-8"))
print("Patched", "OK" if patched != data else "no change")
