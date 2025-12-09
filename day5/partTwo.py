from pathlib import Path

scriptDir = Path(__file__).resolve().parent
inputPath = scriptDir / "input"

with inputPath.open() as f:
    rawData = f.read().strip()

lines = rawData.splitlines()

lims = []
i = 0
while i < len(lines) and lines[i] != "":
    start, end = map(int, lines[i].split("-"))
    lims.append((start, end))
    i += 1

lims.sort()

merged = []
for start, end in lims:
    if merged and start <= merged[-1][1] + 1:
        merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    else:
        merged.append((start, end))

#wait this is decently fast
#prob not the fastest
#but yippe
totalFreshIds = sum(end - start + 1 for start, end in merged)
print(totalFreshIds)