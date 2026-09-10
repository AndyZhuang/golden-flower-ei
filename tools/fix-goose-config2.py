# -*- coding: utf-8 -*-
"""
fix-goose-config2.py

把 goose config.yaml 改为 Goose 1.50.0 真正接受的格式:
- env: 是普通 env vars 字典,会被直接 set 到子进程
- env_keys: 才是 secret lookup (会走 keyring),不能用普通 env path

正确 unicode escape:
- 合 = U+5408
- 曜 = U+66DC
"""
from __future__ import annotations
import sys
from pathlib import Path

GFEI_DIR = "D:/\u5408\u66dcAI/golden-flower-ei"
CONFIG_PATH = Path(r"C:\Users\P1\AppData\Roaming\Block\goose\config\config.yaml")

CONTENT = (
    "# Goose config for GFEI mock-LLM run\n"
    "# Goose 1.50.0 OpenAI provider reads top-level OPENAI_BASE_URL/OPENAI_API_KEY\n"
    "# Extension env: provides plain env vars to child process; env_keys: fetches\n"
    "# from keyring (use only for secrets).\n"
    "GOOSE_PROVIDER: openai\n"
    "GOOSE_MODEL: gpt-4o-mini\n"
    "OPENAI_BASE_URL: http://127.0.0.1:9998/v1\n"
    "OPENAI_API_KEY: sk-mock-no-key-needed\n"
    "extensions:\n"
    "  gfei-mcp:\n"
    "    type: stdio\n"
    "    name: gfei-mcp\n"
    "    cmd: python\n"
    f"    args: [\"{GFEI_DIR}/goose-harness/mcp-server/server.py\"]\n"
    "    envs:\n"
    f"      GFEI_KARMA_DIR: \"{GFEI_DIR}/goose-harness/karma\"\n"
    "      PYTHONIOENCODING: \"utf-8\"\n"
    "    enabled: true\n"
    "    description: \"GFEI MCP\"\n"
)


def main() -> int:
    data = CONTENT.encode("utf-8")
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.write_bytes(data)
    print(f"OK wrote {len(data)} bytes to {CONFIG_PATH}")
    # 验证
    print(CONFIG_PATH.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
