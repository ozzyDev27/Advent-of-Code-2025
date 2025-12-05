import os
from pathlib import Path

scriptDir = Path(__file__).resolve().parent
inputPath = scriptDir / "input"

with inputPath.open() as f:
    rawData = f.read().strip()

lines = rawData.splitlines()
# print(lines)

blankLineHit=False
i=-1
lims=[]
# print(f"$$$$$$$$$$$${lines[1184]}")
while not blankLineHit:
    i+=1
    if lines[i]=="":
        blankLineHit=True
        break
    lims.append((int(lines[i].split("-")[0]),int(lines[i].split("-")[1])))
amountlims=len(lims) #this is faster prob
offset=i+1
# print(f"!!!!!!!!!{i}")
final=0
while i<len(lines)-1:
    i+=1
    print(i)
    for x in range(amountlims):
        if int(lines[i])>=lims[x][0] and int(lines[i])<=lims[x][1]:
            final+=1
            break
print(final)

#it works first try ez