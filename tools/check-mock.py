data = open(r'D:\合曜AI\golden-flower-ei\tools\mock-llm.py', 'rb').read()
i = 0
while True:
    j = data.find(b'n\\u', i)
    if j < 0:
        break
    print('pos', j, repr(data[max(0,j-10):j+25]))
    i = j + 1
