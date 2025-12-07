import os
from pathlib import Path

scriptDir = Path(__file__).resolve().parent
inputPath = scriptDir / "input"

with inputPath.open() as f:
    rawData = f.read().splitlines()

if not rawData:
    print(0)
    exit(0)

maxLen = max(len(l) for l in rawData)
lines = [l.ljust(maxLen) for l in rawData]
rows = len(lines)
cols = maxLen

grid = [list(l) for l in lines]
sepCols = [all(grid[i][j] == ' ' for i in range(rows)) for j in range(cols)]

blocks = []
j = 0
while j < cols:
    if not sepCols[j]:
        s = j
        while j < cols and not sepCols[j]:
            j += 1
        blocks.append((s, j))
    else:
        j += 1

total = 0
for start, end in blocks:
    bot = "".join(grid[rows - 1][start:end])
    opChar = None
    for ch in bot:
        if ch in '+*':
            opChar = ch
            break
    if opChar is None:
        continue

    nums = []
    for j in range(end - 1, start - 1, -1):
        colChars = [grid[i][j] for i in range(rows - 1)]
        s = "".join(colChars).strip()
        if not s:
            continue
        digits = "".join(ch for ch in s if ch.isdigit())
        if not digits:
            continue
        try:
            nums.append(int(digits))
        except ValueError:
            pass

    if not nums:
        continue

    if opChar == '*':
        prod = 1
        for n in nums:
            prod *= n
        total += prod
    else:
        total += sum(nums)

print(total)
