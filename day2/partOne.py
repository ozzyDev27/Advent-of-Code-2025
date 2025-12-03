import os
from pathlib import Path

script_dir = Path(__file__).resolve().parent
candidate = script_dir / "partOne.input"

with candidate.open() as f:
    data = f.read().strip()

invalid = 0
for product_range in data.split(','):
    lower, upper = [int(n) for n in product_range.split('-')]
    for i in range(lower, upper + 1):
        s = str(i)
        if len(s) % 2 == 0 and s[:len(s) // 2] == s[len(s) // 2:]: invalid += i
print(invalid)
