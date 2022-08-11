from sys import stdin,stdout
n = int(stdin.readline())
a = sorted(map(int,stdin.readline().split()))
m = int(stdin.readline())
b = list(map(int,stdin.readline().split()))


idx = n//2

def check(x , y, start, end):
    if start>end:
        return 0
    z = (start+end)//2
    if x == y[z]:
        return 1
    elif x < y[z]:
        return check(x, y, start, z-1)
    else :
        return check(x,y,z+1,end)

for i in range(len(b)):
    start = 0
    end = len(a)-1
    print(check(b[i],a,start,end),end =" ")

            

