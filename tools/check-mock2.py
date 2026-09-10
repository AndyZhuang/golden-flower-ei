data = open(r'D:\合曜AI\golden-flower-ei\tools\mock-llm.py', 'rb').read().decode('utf-8', errors='replace')
lines = data.split('\n')
for i in range(18, 25):
    print(f'{i+1:3}: {repr(lines[i])}')
