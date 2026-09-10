# -*- coding: utf-8 -*-
"""
fix-karma-recipe.py

把 gfei-karma.yaml 的 env_keys 替换为 env dict (Goose 1.50 真正接受)
"""
from __future__ import annotations
import sys
from pathlib import Path

P = Path(r"D:\合曜AI\golden-flower-ei\goose-harness\recipes\gfei-karma.yaml")

OLD = '''extensions:
  - type: stdio
    name: gfei-mcp
    cmd: python
    args: ["goose-harness/mcp-server/server.py"]
    env_keys: ["GFEI_KARMA_DIR"]
'''

NEW = '''extensions:
  - type: stdio
    name: gfei-mcp
    cmd: python
    args: ["goose-harness/mcp-server/server.py"]
    env:
      GFEI_KARMA_DIR: "D:/\u5408\u66dcAI/golden-flower-ei/goose-harness/karma"
      PYTHONIOENCODING: "utf-8"
'''


def main() -> int:
    raw = P.read_bytes()
    s = raw.decode("utf-8")
    if OLD not in s:
        print("OLD block not found — already patched or different format")
        return 1
    s = s.replace(OLD, NEW)
    P.write_bytes(s.encode("utf-8"))
    print(f"OK patched {P}")
    # verify
    print(P.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
