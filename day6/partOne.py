import os
from pathlib import Path

scriptDir = Path(__file__).resolve().parent
inputPath = scriptDir / "input"

with inputPath.open() as f:
    rawData = f.read().splitlines()

maxlen = max(len(l) for l in rawData)
lines = [l.ljust(maxlen) for l in rawData]
rows = len(lines)
cols = maxlen

grid = [list(l) for l in lines]

sepCols = [all(grid[i][j] == ' ' for i in range(rows)) for j in range(cols)]

blocks = []
j = 0
while j < cols:
    if not sepCols[j]:
        start = j
        while j < cols and not sepCols[j]:
            j += 1
        blocks.append((start, j))
    else:
        j += 1

total = 0
for start, end in blocks:
    colsStr = ["".join(grid[i][start:end]).strip() for i in range(rows)]

    opChar = None
    bot = colsStr[-1]
    if bot in ('+', '*'):
        opChar = bot
    else:
        for ch in bot:
            if ch in ('+', '*'):
                opChar = ch
                break
    if opChar is None:
        for j in range(start, end):
            if grid[rows - 1][j] in ('+', '*'):
                opChar = grid[rows - 1][j]
                break
    if opChar is None:
        continue

    nums = []
    for rowStr in colsStr[:-1]:
        if not rowStr:
            continue
        for part in rowStr.split():
            try:
                nums.append(int(part))
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