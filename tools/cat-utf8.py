import sys
from pathlib import Path
p = Path(sys.argv[1])
b = p.read_bytes()
sys.stdout.buffer.write(b)
sys.stdout.buffer.write(b'\n')
