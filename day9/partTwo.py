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

# Build boundaries for each row (y coordinate)
# Each row tracks the min and max x coordinates that are valid (green or red)
boundaries = {}

for i in range(len(redTiles)):
    xOne, yOne = redTiles[i]
    xTwo, yTwo = redTiles[(i + 1) % len(redTiles)]
    
    if xOne == xTwo:
        # Vertical edge - same x, different y
        for y in range(min(yOne, yTwo), max(yOne, yTwo) + 1):
            if y not in boundaries:
                boundaries[y] = [xOne, xOne]
            else:
                boundaries[y][0] = min(boundaries[y][0], xOne)
                boundaries[y][1] = max(boundaries[y][1], xOne)
    else:
        # Horizontal edge - same y, different x
        if yOne not in boundaries:
            boundaries[yOne] = [min(xOne, xTwo), max(xOne, xTwo)]
        else:
            boundaries[yOne][0] = min(boundaries[yOne][0], xOne, xTwo)
            boundaries[yOne][1] = max(boundaries[yOne][1], xOne, xTwo)

maxArea = 0

for i in range(len(redTiles)):
    for j in range(i + 1, len(redTiles)):
        xOne, yOne = redTiles[i]
        xTwo, yTwo = redTiles[j]
        
        minX = min(xOne, xTwo)
        maxX = max(xOne, xTwo)
        minY = min(yOne, yTwo)
        maxY = max(yOne, yTwo)
        
        # Check if this rectangle fits within the boundaries
        valid = True
        for y in range(minY, maxY + 1):
            if y not in boundaries:
                valid = False
                break
            boundMinX, boundMaxX = boundaries[y]
            if minX < boundMinX or maxX > boundMaxX:
                valid = False
                break
        
        if valid:
            width = maxX - minX + 1
            height = maxY - minY + 1
            area = width * height
            
            if area > maxArea:
                maxArea = area

print(maxArea)
#oh my god bro finally
#52 MINUTES
# AND ITS SO SLOW
# BUT IT WORKS