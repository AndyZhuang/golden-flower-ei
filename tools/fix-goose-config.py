# -*- coding: utf-8 -*-
"""
fix-goose-config.py

用 UTF-8 重写 Goose config.yaml,把 providers.openai.parameters.base_url
错误嵌套改掉,改为 Goose 1.50.0 实际读取的顶层 OPENAI_BASE_URL +
OPENAI_API_KEY 字段。中文路径仍用 \\uXXXX escape 防止 PowerShell 5.1
GBK 二次污染写入。
"""

from __future__ import annotations
import sys
from pathlib import Path

# \u escape 中文字符,避开 PowerShell Set-Content 走 GBK
GFEI_DIR = "D:/\u5408\u6656AI/golden-flower-ei"

CONFIG_PATH = Path(
    r"C:\Users\P1\AppData\Roaming\Block\goose\config\config.yaml"
)

# 干净 UTF-8 YAML 内容(Goose 1.50 实际读的字段)
CONTENT = (
    "# Goose config for GFEI mock-LLM run\n"
    "# Goose 1.50.0 OpenAI provider 读顶层 OPENAI_BASE_URL / OPENAI_API_KEY,\n"
    "# 不读 providers.openai.parameters.base_url 嵌套路径。\n"
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
    "    env_keys: [\"GFEI_KARMA_DIR\", \"PYTHONIOENCODING\"]\n"
    "    env:\n"
    f"      GFEI_KARMA_DIR: \"{GFEI_DIR}/goose-harness/karma\"\n"
    "      PYTHONIOENCODING: \"utf-8\"\n"
    "    enabled: true\n"
    "    description: \"GFEI MCP\"\n"
)


def main() -> int:
    # 显式 UTF-8 no-BOM,Goose YAML parser 接受
    data = CONTENT.encode("utf-8")
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.write_bytes(data)
    print(f"OK wrote {len(data)} bytes to {CONFIG_PATH}")
    # 回显确认
    print("--- file content ---")
    print(CONFIG_PATH.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
