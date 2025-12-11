import os

scriptDir = os.path.dirname(os.path.abspath(__file__))

with open("input") as f:
    rawData = f.read().strip()

lines = rawData.splitlines()

graph = {}
for i in range(len(lines)):
    parts = lines[i].split(': ')
    device = parts[0]
    outputs = parts[1].split()
    graph[device] = outputs

memo = {}

def countPaths(current, target, visited, hasDac, hasFft):
    if current == 'dac':
        hasDac = True
    if current == 'fft':
        hasFft = True
    
    if current == target:
        return 1 if (hasDac and hasFft) else 0
    
    if current in visited or current not in graph:
        return 0
    
    key = (current, hasDac, hasFft, frozenset(visited))
    if key in memo:
        return memo[key]
    
    visited.add(current)
    totalPaths = 0
    
    for j in range(len(graph[current])):
        totalPaths += countPaths(graph[current][j], target, visited, hasDac, hasFft)
    
    visited.remove(current)
    
    memo[key] = totalPaths
    return totalPaths

pathCount = countPaths('svr', 'out', set(), False, False)
print(pathCount)


#so fast wow
#its so fast you can even do your math homework and studying and also watch some youtube while its running
