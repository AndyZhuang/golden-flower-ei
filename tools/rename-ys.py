# -*- coding: utf-8 -*-
"""
rename-ys.py

把 YS 项目的中文 display name 从 "养神" 改为 "Y神" (拼音首字母 + 神)。
英文仍保留 "Yang Shen" (拼音, 对应阳神)。
"""
from __future__ import annotations
import sys
from pathlib import Path

I18N = Path(r"D:\合曜AI\golden-flower-ei\lib\i18n.tsx")
PAGE = Path(r"D:\合曜AI\golden-flower-ei\app\page.tsx")


def main() -> int:
    # i18n.tsx
    s = I18N.read_text(encoding="utf-8")
    # 养神 = \u517b\u795e
    OLD_ZH = '"home.projects.ys.name": "\u517b\u795e",'
    NEW_ZH = '"home.projects.ys.name": "Y\u795e",'
    if OLD_ZH not in s:
        print("OLD_ZH not found")
        return 1
    s = s.replace(OLD_ZH, NEW_ZH, 1)
    I18N.write_text(s, encoding="utf-8")
    print(f"OK patched {I18N}")
    # page.tsx - num prop 来自 i18n t(), 所以不需要改 page.tsx
    # 但 ProjectCard 组件里 en="Yang Shen" 是字面量,保留
    # 验证
    page = PAGE.read_text(encoding="utf-8")
    i18n = I18N.read_text(encoding="utf-8")
    assert "Y\u795e" in i18n, "Y神 not in i18n"
    assert "Yang Shen" in page, "Yang Shen not in page"
    print("verify OK: i18n has Y神, page has Yang Shen")
    return 0


if __name__ == "__main__":
    sys.exit(main())