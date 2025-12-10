import os
from pathlib import Path
import re

script_dir = Path(__file__).resolve().parent
candidate = script_dir / "input"

with candidate.open() as f:
    data = f.read().strip()

lines = data.splitlines()

totalPresses = 0

for line in lines:
    parts = re.findall(r'\[([.#]+)\]|(\([0-9,]+\))|\{[0-9,]+\}', line) #regex actually being useful for once?!?!?!?!
    
    targetStr = [p[0] for p in parts if p[0]][0]
    target = [1 if c == '#' else 0 for c in targetStr]
    numLights = len(target)
    
    buttonStrs = [p[1] for p in parts if p[1]]
    buttons = []
    for btnStr in buttonStrs:
        indices = list(map(int, btnStr.strip('()').split(',')))
        button = [0] * numLights
        for idx in indices:
            button[idx] = 1
        buttons.append(button)
    
    numButtons = len(buttons)
    minPresses = 1000000000000000000000000
    for mask in range(1 << numButtons):
        state = [0] * numLights
        presses = 0
        
        for i in range(numButtons):
            if mask & (1 << i):
                presses += 1
                for j in range(numLights):
                    state[j] ^= buttons[i][j]
        
        if state == target:
            minPresses = min(minPresses, presses)
    
    totalPresses += minPresses

print(totalPresses)