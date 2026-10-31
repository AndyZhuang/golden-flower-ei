import re
from pathlib import Path

HTML = Path(r'D:\合曜AI\golden-flower-ei\docs\business-plan.html')
MD = Path(r'D:\合曜AI\golden-flower-ei\docs\business-plan.md')

h = HTML.read_text(encoding='utf-8')
m = MD.read_text(encoding='utf-8')

# --- HTML structure checks ---
checks = {
    'doctype': h.startswith('<!DOCTYPE html>'),
    'has </html>': h.rstrip().endswith('</html>'),
    'style closed': h.count('<style>') == 1 and h.count('</style>') == 1,
    'body closed': h.count('<body>') == 1 and h.count('</body>') == 1,
    'no replacement char': '\ufffd' not in h,
}
# tag balance for key containers
for tag in ['div', 'section', 'table', 'p', 'ul', 'ol', 'li', 'tr', 'td', 'th', 'blockquote']:
    opens = len(re.findall(rf'<{tag}[\s>]', h))
    closes = len(re.findall(rf'</{tag}>', h))
    checks[f'balance <{tag}>'] = (opens == closes, f'{opens} open / {closes} close')

print('=== HTML ===')
for k, v in checks.items():
    if isinstance(v, tuple):
        print(f'  {"OK " if v[0] else "FAIL"} {k}: {v[1]}')
    else:
        print(f'  {"OK " if v else "FAIL"} {k}')

# --- content checks (both files) ---
print('\n=== content ===')
must = [
    ('Deqi', 'Deqi'),
    ('XG', 'XG'),
    ('YS', 'YS'),
    ('ME methodology', 'ME methodology'),
    ('moral evaluation', 'moral evaluation'),
    ('foundation model paradigm', 'foundation model'),
    ('Article 99', 'Article 99'),
    ('7%', '7%'),
    ('76.5%', '76.5%'),
    ('$1.5M', '$1.5M'),
    ('$3.44M', '$3.44M'),
    ('karma ledger', 'karma'),
    ('18%', '18%'),
]
for label, needle in must:
    print(f'  {"OK " if needle in h else "FAIL"} html has {label}')

print('\n=== chinese integrity ===')
for p in (HTML, MD):
    s = p.read_text(encoding='utf-8')
    cn = sum(1 for c in s if '\u4e00' <= c <= '\u9fff')
    print(f'  {p.name}: {cn} chinese chars, mojibake={"\ufffd" in s}')

print('\n=== anchors vs ids ===')
anchors = set(re.findall(r'href="#([^"]+)"', h))
ids = set(re.findall(r'id="([^"]+)"', h))
missing = anchors - ids
print(f'  {len(anchors)} anchors, {len(ids)} ids, missing: {missing if missing else "none"}')

print('\n=== md ===')
print(f'  {len(m.splitlines())} lines, {len(m)} chars')
print(f'  headings: {len(re.findall(r"^#+ ", m, re.M))}')
