import os
from pathlib import Path

scriptDir = Path(__file__).resolve().parent
inputPath = scriptDir / "input"

with inputPath.open() as f:
    rawData = f.read().strip()

lines = rawData.splitlines()
paperGrid = [list(line) for line in lines]
adjacentOffsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
numRows = len(paperGrid)
numCols = len(paperGrid[0]) if numRows else 0

accessibleRolls = 0
for row in range(numRows):
    for col in range(numCols):
        if paperGrid[row][col] != '@':
            continue
        adjacentCount = 0
        for dRow, dCol in adjacentOffsets:
            nRow, nCol = row + dRow, col + dCol
            if 0 <= nRow < numRows and 0 <= nCol < numCols and paperGrid[nRow][nCol] == '@':
                adjacentCount += 1
        if adjacentCount < 4:
            accessibleRolls += 1

print(accessibleRolls)
