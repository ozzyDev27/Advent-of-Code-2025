from pathlib import Path

script_dir = Path(__file__).resolve().parent
input_file = script_dir / "input"

with input_file.open() as f:
    grid = [line.rstrip('\n') for line in f]

startBeam = grid[0].index('S')
beams = {startBeam}
splits = 0

for i in range(1, len(grid)):
    newBeams = set()
    
    for j in beams:
        if grid[i][j] == '^':
            splits += 1
            if j - 1 >= 0:
                newBeams.add(j - 1)
            if j + 1 < len(grid[0]):
                newBeams.add(j + 1)
        else:
            newBeams.add(j)
    
    beams = newBeams
    
    if not beams:
        break

print(splits)