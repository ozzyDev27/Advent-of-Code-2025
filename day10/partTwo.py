import os
from pathlib import Path
import re
from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np
from math import ceil

script_dir = Path(__file__).resolve().parent
candidate = script_dir / "input"

with candidate.open() as f:
    data = f.read().strip()

lines = data.splitlines()

totalPresses = 0

for line in lines:
    parts = re.findall(r'\[([.#]+)\]|(\([0-9,]+\))|\{([0-9,]+)\}', line)
    
    joltageStr = [p[2] for p in parts if p[2]][0]
    target = list(map(int, joltageStr.split(',')))
    numCounters = len(target)
    
    buttonStrs = [p[1] for p in parts if p[1]]
    buttons = []
    for i in buttonStrs:
        indices = list(map(int, i.strip('()').split(',')))
        button = [0] * numCounters
        for j in indices:
            button[j] = 1
        buttons.append(button)
    
    numButtons = len(buttons)
    
    A = np.array([[buttons[i][j] for i in range(numButtons)] for j in range(numCounters)])
    b = np.array(target)
    c = np.ones(numButtons)
    constraints = LinearConstraint(A, b, b)
    bounds = Bounds(0, np.inf)
    result = milp(c, constraints=constraints, bounds=bounds, integrality=np.ones(numButtons))
    
    totalPresses += ceil(np.sum(result.x))

print(totalPresses)