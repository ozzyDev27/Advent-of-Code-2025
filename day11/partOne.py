import os
from pathlib import Path

scriptDir = Path(__file__).resolve().parent
inputPath = scriptDir / "input"

with inputPath.open() as f:
    rawData = f.read().strip()

lines = rawData.splitlines()

graph = {}
for i in range(len(lines)):
    parts = lines[i].split(': ')
    device = parts[0]
    outputs = parts[1].split()
    graph[device] = outputs

memo = {}

def countPaths(current, target, visited):
    if current == target:
        return 1
    
    if current in visited or current not in graph:
        return 0
    
    key = (current, frozenset(visited))
    if key in memo:
        return memo[key]
    
    visited.add(current)
    totalPaths = 0
    
    for j in range(len(graph[current])):
        totalPaths += countPaths(graph[current][j], target, visited)
    
    visited.remove(current)
    
    memo[key] = totalPaths
    return totalPaths

pathCount = countPaths('you', 'out', set())
print(pathCount)
