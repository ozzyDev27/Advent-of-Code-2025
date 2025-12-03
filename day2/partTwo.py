import os
from pathlib import Path

script_dir = Path(__file__).resolve().parent
candidate = script_dir / "partOne.input"

with candidate.open() as f:
    data = f.read().strip()

invalid = 0
for product_range in data.split(','):
    lower, upper = [int(n) for n in product_range.split('-')]
    for i in range(max(lower, 10), upper + 1):
        s = str(i)
        for j in (k for k in range(1, int(len(s) ** .5) + 1) if len(s) % k == 0):
            if s[:j] * (len(s) // j) == s or (j != 1 and s[:len(s) // j] * j == s):
                invalid += i
                break
print(invalid)
