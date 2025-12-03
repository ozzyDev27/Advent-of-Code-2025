import os
from pathlib import Path

script_dir = Path(__file__).resolve().parent
candidate = script_dir / "partOne.input"

with candidate.open() as f:
    data = f.read()
    
# 100 x 200 yayayaya
sum=0
amount=12
for bank in data.strip().split("\n"):
    locs=[0 for i in range(amount)]
    for i in range(101-amount):#first one :checkmark: (makes it much easier for me lol)
        if bank[i]>bank[locs[0]]:
            locs[0]=i
    
    for i in range(1,amount):
        locs[i]=locs[i-1]+1
        for battery in range(locs[i-1]+1,(101-amount)+i):
            if bank[battery]>bank[locs[i]]:
                locs[i]=battery
    # print(f"{bank[locs[0]]}{bank[locs[1]]}")
    print(int("".join([str(bank[locs[i]]) for i in range(12)])))
    sum+=int("".join([str(bank[locs[i]]) for i in range(12)]))
    # sum+=int(str(bank[locs[0]])+str(bank[locs[1]]))
print(sum)