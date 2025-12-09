import os
from pathlib import Path

scriptDir = Path(__file__).resolve().parent
inputPath = scriptDir / "input"

with inputPath.open() as f:
    rawData = f.read().strip()

lines = rawData.splitlines()

redTiles = []
for line in lines:
    coords = line.split(',')
    x = int(coords[0])
    y = int(coords[1])
    redTiles.append((x, y))

maxArea = 0

for i in range(len(redTiles)):
    for j in range(i+1, len(redTiles)):
        xOne, yOne = redTiles[i]
        xTwo, yTwo = redTiles[j]
        
        width = abs(xTwo - xOne) + 1
        height = abs(yTwo - yOne) + 1
        area = width * height
        
        if area > maxArea:
            maxArea = area

print(maxArea)