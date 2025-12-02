
while False:
    print(int(input("> "))%100)
initial = 1
while True:
    dial=int(input("> "))

    final=0
    if dial==0:
        final+=1
    elif dial>=100:
        final+=abs(dial//100)
    elif dial<0:
        final+=(abs(dial)//100)
        final+=initial!=0

    print(final)