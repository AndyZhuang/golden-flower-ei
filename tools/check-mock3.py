data = open(r'D:\合曜AI\golden-flower-ei\tools\mock-llm.py', 'rb').read()
i = data.find('我是'.encode('utf-8'))
print('First Chinese at byte', i)
print('Bytes 280-440:')
import binascii
print(binascii.hexlify(data[280:440]).decode())
print('Decoded:', repr(data[280:440].decode('utf-8', errors='replace')))
