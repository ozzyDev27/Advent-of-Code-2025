import os
from pathlib import Path

script_dir = Path(__file__).resolve().parent
candidate = script_dir / "partOne.input"

with candidate.open() as f:
    data = f.read().strip().split("\n")

dial=50
final=0
for lineNum in range(len(data)):
    dial%=100
    before=dial
    dial+=int(data[lineNum][1:]) * (((data[lineNum][0]=="R")*2)-1)
    if dial==0:
        final+=1
    elif dial>=100:
        final+=abs(dial//100)
    elif dial<0:
        final+=(abs(dial)//100)
        final+=before!=0
    #stupid stupid edge cases :(

print(final)