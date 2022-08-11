import sys
yutlist = [list(map(int,sys.stdin.readline().split())) for i in range(3)]
for i in range(3) :
    if sum(yutlist[i]) == 0:
        print("D")
    elif sum(yutlist[i]) == 1:
        print("C")
    elif sum(yutlist[i]) == 2:
        print("B")
    elif sum(yutlist[i]) == 3:
        print("A")
    elif sum(yutlist[i]) == 4:
        print("E")