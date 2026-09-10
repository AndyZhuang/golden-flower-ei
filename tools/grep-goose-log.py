import re, sys
path = r'C:\Users\P1\AppData\Roaming\Block\goose\data\logs\cli\2026-09-10\20260910_084713.log'
b = open(path, 'rb').read()
print('total bytes:', len(b))
print('--- raw decoded ---')
sys.stdout.buffer.write(b)
print()
print('--- keywords ---')
for kw in [b'empty', b'Error', b'timeout', b'response', b'fail', b'stream', b'mock', b'minimal']:
    matches = [m.start() for m in re.finditer(kw, b, re.IGNORECASE)]
    if matches:
        for pos in matches[:3]:
            start = max(0, pos - 100)
            end = min(len(b), pos + 300)
            print(f'KW={kw!r} at {pos}: ...{b[start:end].decode("utf-8", errors="replace")}...')
            print('---')
