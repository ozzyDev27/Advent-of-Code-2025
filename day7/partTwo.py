from pathlib import Path

scriptDir = Path(__file__).resolve().parent
inputFile = scriptDir / "input"

with inputFile.open() as f:
    grid = [line.rstrip('\n') for line in f]

startBeam = grid[0].index('S')
timelines = {startBeam: 1}

for i in range(1, len(grid)):
    newTimelines = {}
    
    for j, count in timelines.items():
        if grid[i][j] == '^':
            if j - 1 >= 0:
                newTimelines[j - 1] = newTimelines.get(j - 1, 0) + count
            if j + 1 < len(grid[0]):
                newTimelines[j + 1] = newTimelines.get(j + 1, 0) + count
        else:
            newTimelines[j] = newTimelines.get(j, 0) + count
    
    timelines = newTimelines
    
    if not timelines:
        break

print(sum(timelines.values()))
