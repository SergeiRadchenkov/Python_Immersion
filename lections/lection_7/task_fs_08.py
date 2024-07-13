import os
from pathlib import Path

print(os.listdir())

p = Path(Path().cwd())
for obg in p.iterdir():
    print(obg)
