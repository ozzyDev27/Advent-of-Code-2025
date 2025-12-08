import os
from pathlib import Path

scriptDir = Path(__file__).resolve().parent
inputPath = scriptDir / "input"

with inputPath.open() as f:
    rawData = f.read().strip()

lines = rawData.splitlines()

junctionBoxes = []
for line in lines:
    coords = line.split(",")
    junctionBoxes.append((int(coords[0]), int(coords[1]), int(coords[2])))

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
    return True

def countCircuits():
    roots = set()
    for i in range(numBoxes):
        roots.add(findRoot(i))
    return len(roots)

lastBoxA = -1
lastBoxB = -1

for i in range(len(edges)):
    dist, boxA, boxB = edges[i]
    
    if unionCircuits(boxA, boxB):
        lastBoxA = boxA
        lastBoxB = boxB
        
        if countCircuits() == 1:
            break

result = junctionBoxes[lastBoxA][0] * junctionBoxes[lastBoxB][0]
print(result)
