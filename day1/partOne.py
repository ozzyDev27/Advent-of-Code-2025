import os
from pathlib import Path

script_dir = Path(__file__).resolve().parent
candidate = script_dir / "partOne.input"

with candidate.open() as f:
    data = f.read().strip().split("\n")

dial=50
final=0
for lineNum in range(len(data)):
    dial+=int(data[lineNum][1:]) * (((data[lineNum][0]=="R")*2)-1)
    dial%=100
    final+=dial==0

print(final)