# inbuilt module -> pathlib

from pathlib import Path

path = Path('ecommerce')

for file in path.glob('*.*'):
    print(file)
