import os
from pathlib import Path

scriptDir = Path(__file__).resolve().parent
inputPath = scriptDir / "input"

with inputPath.open() as f:
    rawData = f.read().strip()

lines = rawData.splitlines()

junctionBoxes = []
for line in lines:
    coords = line.split(',')
    x = int(coords[0])
    y = int(coords[1])
    z = int(coords[2])
    junctionBoxes.append((x, y, z))

numBoxes = len(junctionBoxes)

def distSquared(box1, box2):
    dx = box1[0] - box2[0]
    dy = box1[1] - box2[1]
    dz = box1[2] - box2[2]
    return dx * dx + dy * dy + dz * dz

edges = []
for i in range(numBoxes):
    for j in range(i + 1, numBoxes):
        dist = distSquared(junctionBoxes[i], junctionBoxes[j])
        edges.append((dist, i, j))

edges.sort()

parent = list(range(numBoxes))
circuitSize = [1] * numBoxes

def findRoot(x):
    if parent[x] != x:
        parent[x] = findRoot(parent[x])
    return parent[x]

def unionCircuits(x, y):
    rootX = findRoot(x)
    rootY = findRoot(y)
    
    if rootX == rootY:
        return False
    
    parent[rootY] = rootX
    circuitSize[rootX] += circuitSize[rootY]
    return True

pairsConnected = 0
for i in range(len(edges)):
    dist, boxA, boxB = edges[i]
    pairsConnected += 1
    unionCircuits(boxA, boxB)
    
    if pairsConnected == 1000:
        break

rootCounts = {}
for i in range(numBoxes):
    root = findRoot(i)
    if root not in rootCounts:
        rootCounts[root] = 0
    rootCounts[root] += 1

finalCircuitSizes = sorted(rootCounts.values())[::-1]

result = finalCircuitSizes[0] * finalCircuitSizes[1] * finalCircuitSizes[2]
print(result)
