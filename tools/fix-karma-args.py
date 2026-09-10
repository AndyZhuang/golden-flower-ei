import sys
p = r'D:\合曜AI\golden-flower-ei\goose-harness\recipes\gfei-karma.yaml'
b = open(p, 'rb').read()
s = b.decode('utf-8')
old = 'args: ["goose-harness/mcp-server/server.py"]'
new = 'args: ["D:/' + '\u5408\u66dc' + 'AI/golden-flower-ei/goose-harness/mcp-server/server.py"]'
if old not in s:
    print('OLD not found, current args lines:')
    for line in s.split('\n'):
        if 'args' in line:
            print('  ', line)
    sys.exit(1)
s = s.replace(old, new)
open(p, 'wb').write(s.encode('utf-8'))
print('OK patched, new content:')
print(s)
