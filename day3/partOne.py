import os
from pathlib import Path

script_dir = Path(__file__).resolve().parent
candidate = script_dir / "partOne.input"

with candidate.open() as f:
    data = f.read()
    
# 100 x 200 yayayaya
sum=0
for bank in data.strip().split("\n"):
    max=0
    for battery in range(99):
        if bank[battery]>bank[max]:
            max=battery
    newmax=max+1
    for battery in range(max+1,100):
        if bank[battery]>bank[newmax]:
            newmax=battery
    print(f"{bank[max]} {bank[newmax]}")
    sum+=int(str(bank[max])+str(bank[newmax]))
print(sum)