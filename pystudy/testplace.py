import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b , c = map(int, sys.stdin.readline().split())
sumValue = int(0)
for i in range(n):
    v = int(a[i])
    check = 0
    number = 0
    v = v - b
    if v <=0:
        number = 0
    elif v%c == 0:
        number =  (v//c)
    else :
        number = (v//c)+1
    sumValue = sumValue + number+1    
print(sumValue)
        
