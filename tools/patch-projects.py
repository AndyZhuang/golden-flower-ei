# -*- coding: utf-8 -*-
"""
patch-projects.py

在 lib/i18n.tsx 增加 3 个项目 (Deqi / XG / YS) 的 i18n key,
在 app/page.tsx 增加 Project section。

描述 (用户要求):
- Deqi (得气) - 原 GFEI harness 项目
- XG (玄关) - 正要开发的整体控制项目,不要提 paseo
- YS (养神) - 有道德层的大模型
- 先不做 github 链接
- 都在研发状态

中文 unicode escape 防 PowerShell 5.1 GBK 污染。
"""

from __future__ import annotations
import sys
from pathlib import Path

I18N = Path(r"D:\合曜AI\golden-flower-ei\lib\i18n.tsx")
PAGE = Path(r"D:\合曜AI\golden-flower-ei\app\page.tsx")


# ============ lib/i18n.tsx ============
# 在 "home.entrance.dialogue.body" 之后插入 home.projects.* keys
# 在 en: 中对应位置插入

NEW_ZH_KEYS = (
    '    "home.projects.title": "\u4e09\u4e2a\u6b63\u5728\u7814\u53d1\u7684\u9879\u76ee",\n'
    '    "home.projects.subtitle": "Three Projects in the Making",\n'
    '    "home.projects.status.research": "\u7814\u53d1\u4e2d",\n'
    '    "home.projects.deqi.name": "\u5f97\u6c14",\n'
    '    "home.projects.deqi.body":\n'
    '      "\u91d1\u82b1 EI \u7684\u5de5\u7a0b\u5316\u5c42\u3002\u4fee\u884c\u8005\u4eba\u683c + \u4fee\u884c\u5bf9\u8bdd + \u591a agent \u6d8c\u73b0\u5267\u672c + Karma \u8d21\u732e\u4f53\u7cfb\u3002\u8ba9\u4f60\u80fd\u95ee AI \u4e00\u4e2a\u771f\u95ee\u9898\uff0c\u7136\u540e\u770b\u89c1\u56de\u7167\u3002",\n'
    '    "home.projects.xg.name": "\u7384\u5173",\n'
    '    "home.projects.xg.body":\n'
    '      "\u5bf9\u591a\u4e2a AI agent\u3001\u6a21\u578b\u3001\u5de5\u5177\u7684\u603b\u4f53\u7f16\u6392\u4e0e\u63a7\u5236\u3002\u4f4d\u4e8e EI \u4e4b\u4e0b\u7684\u201c\u8c03\u5ea6\u5c42\u201d\u2014\u2014\u5c06\u610f\u56fe\u8f6c\u5316\u4e3a\u53ef\u6267\u884c\u7684\u591a\u65b9\u534f\u4f5c\uff0c\u8ba9\u4e0d\u540c\u7684\u667a\u80fd\u5404\u5f97\u5176\u6240\u3002",\n'
    '    "home.projects.ys.name": "\u517b\u795e",\n'
    '    "home.projects.ys.body":\n'
    '      "\u6709\u5185\u5728\u9053\u5fb7\u5c42\u7684\u5927\u6a21\u578b\u3002\u4e0d\u662f\u5bf9\u9f50\u5728\u5916\u5c42\u89c4\u5219\u4e4b\u4e0a\uff0c\u800c\u662f\u5728\u6a21\u578b\u7684\u8ba4\u77e5\u6df1\u5904\u5d4c\u5165\u4ef7\u503c\u5224\u65ad\u4e0e\u884c\u4e3a\u5bf9\u5e94\u2014\u2014\u8ba9\u5b83\u5728\u601d\u8003\u65f6\u5c31\u8003\u8651\u201c\u8fd9\u4ef6\u4e8b\u8be5\u4e0d\u8be5\u505a\u201d\u3002",\n'
)

NEW_EN_KEYS = (
    '    "home.projects.title": "Three Projects in the Making",\n'
    '    "home.projects.subtitle": "Three Projects in the Making",\n'
    '    "home.projects.status.research": "In development",\n'
    '    "home.projects.deqi.name": "Deqi",\n'
    '    "home.projects.deqi.body":\n'
    '      "The engineering layer of Golden Flower EI. Practitioner persona + practice dialogue + multi-agent emergence script + Karma contribution system. Ask AI a real question, then see the reflection.",\n'
    '    "home.projects.xg.name": "Xuan Guan",\n'
    '    "home.projects.xg.body":\n'
    '      "An overall orchestration and control layer for multiple AI agents, models, and tools. The dispatch layer under EI: turning intent into executable multi-party collaboration, letting each intelligence find its place.",\n'
    '    "home.projects.ys.name": "Yang Shen",\n'
    '    "home.projects.ys.body":\n'
    '      "A large model with an inner moral layer. Not alignment as an outer rule, but value judgment and behavioral correspondence embedded deep in the model\u2019s cognition \u2014 so it considers \\"should this be done\\" as it thinks.",\n'
)


def patch_i18n() -> None:
    s = I18N.read_text(encoding="utf-8")
    # 在 zh: 块末尾、en: 块开头前插入 zh keys
    # 用 dialog.dict 锚点 - "dialogue.suggested" 在 zh 中存在
    ZH_ANCHOR = '"dialogue.principles": "\u4fee\u884c\u5bf9\u8bdd \u00b7 \u4e09\u6761\u539f\u5219",'
    if ZH_ANCHOR not in s:
        print(f"ZH anchor not found, file unchanged")
        return
    # 找 zh 块范围 - 从 "site.title": 开始到 "use 1" (Lang type) 之前
    # 我们插入在 "home.entrance.emergence.body" 那行后面
    ZH_INSERT_AT = '"emergence.start": "\u25b6 \u5f00\u59cb\u89c2\u5bdf",'
    if ZH_INSERT_AT not in s:
        # 备选锚点 - 找 emergence.start
        print("emergence.start zh not found, using emergence.start anchor")
    s = s.replace(ZH_INSERT_AT, NEW_ZH_KEYS + ZH_INSERT_AT, 1)
    # 英文块同样
    EN_INSERT_AT = '"emergence.start": "\u25b6 Start Watching",'
    if EN_INSERT_AT not in s:
        print("emergence.start en not found")
        return
    s = s.replace(EN_INSERT_AT, NEW_EN_KEYS + EN_INSERT_AT, 1)
    I18N.write_text(s, encoding="utf-8")
    print(f"OK patched {I18N}")


# ============ app/page.tsx ============

# 在 quote section 之前插入 Project section
PROJECT_SECTION = (
    '      <section className="relative max-w-6xl mx-auto px-6 py-24">\n'
    '        <div className="text-center mb-16">\n'
    '          <div className="text-[10px] tracking-[0.5em] uppercase text-gold-300/60 mb-3">\n'
    '            {t("home.projects.subtitle")}\n'
    '          </div>\n'
    '          <h2 className="text-3xl md:text-4xl font-serif font-light text-gold-50 text-balance">\n'
    '            {t("home.projects.title")}\n'
    '          </h2>\n'
    '        </div>\n'
    '        <div className="grid md:grid-cols-3 gap-6">\n'
    '          <ProjectCard\n'
    '            num={t("home.projects.deqi.name")}\n'
    '            en="Deqi"\n'
    '            body={t("home.projects.deqi.body")}\n'
    '            status={t("home.projects.status.research")}\n'
    '          />\n'
    '          <ProjectCard\n'
    '            num={t("home.projects.xg.name")}\n'
    '            en="Xuan Guan"\n'
    '            body={t("home.projects.xg.body")}\n'
    '            status={t("home.projects.status.research")}\n'
    '          />\n'
    '          <ProjectCard\n'
    '            num={t("home.projects.ys.name")}\n'
    '            en="Yang Shen"\n'
    '            body={t("home.projects.ys.body")}\n'
    '            status={t("home.projects.status.research")}\n'
    '          />\n'
    '        </div>\n'
    '      </section>\n'
    '\n'
)

PROJECT_CARD_COMPONENT = (
    '\n'
    'function ProjectCard({\n'
    '  num,\n'
    '  en,\n'
    '  body,\n'
    '  status,\n'
    '}: {\n'
    '  num: string;\n'
    '  en: string;\n'
    '  body: string;\n'
    '  status: string;\n'
    '}) {\n'
    '  return (\n'
    '    <div className="relative p-6 rounded-2xl border border-gold-700/20 bg-ink-900/40 backdrop-blur-sm hover:border-gold-400/40 transition-all duration-500 group">\n'
    '      <div className="absolute top-4 right-4 px-2.5 py-1 rounded-full border border-gold-700/40 text-[10px] tracking-widest uppercase text-gold-300/60">\n'
    '        {status}\n'
    '      </div>\n'
    '      <div className="text-4xl font-serif text-gold-300/40 mb-3 group-hover:text-gold-300/70 transition-colors">\n'
    '        {num}\n'
    '      </div>\n'
    '      <div className="text-[10px] tracking-[0.3em] uppercase text-gold-300/40 mb-3">\n'
    '        {en}\n'
    '      </div>\n'
    '      <h3 className="text-lg font-serif text-gold-50 mb-3 leading-snug">\n'
    '        {en}\n'
    '      </h3>\n'
    '      <p className="text-amber-100/60 leading-relaxed text-sm">{body}</p>\n'
    '    </div>\n'
    '  );\n'
    '}\n'
)


def patch_page() -> None:
    s = PAGE.read_text(encoding="utf-8")
    # 在 quote section 之前插入 Project section
    QUOTE_ANCHOR = '<section className="relative max-w-3xl mx-auto px-6 py-24 text-center">'
    if QUOTE_ANCHOR not in s:
        print("quote anchor not found")
        return
    # 把 PROJECT_SECTION 插到 QUOTE_ANCHOR 之前
    if "home.projects.title" in s:
        print("already patched")
        return
    s = s.replace(QUOTE_ANCHOR, PROJECT_SECTION + "      " + QUOTE_ANCHOR, 1)
    # 在文件末尾 (function Proposition 之后) 添加 ProjectCard
    s = s.replace(
        '    </div>\n  );\n}\n',
        '    </div>\n  );\n}\n' + PROJECT_CARD_COMPONENT,
        1,
    )
    PAGE.write_text(s, encoding="utf-8")
    print(f"OK patched {PAGE}")


def main() -> int:
    patch_i18n()
    patch_page()
    # 验证
    page = PAGE.read_text(encoding="utf-8")
    i18n = I18N.read_text(encoding="utf-8")
    assert "home.projects.deqi.body" in i18n
    assert "Deqi" in page
    assert "ProjectCard" in page
    print("verify OK: i18n has home.projects.* keys, page has ProjectCard")
    return 0


if __name__ == "__main__":
    sys.exit(main())