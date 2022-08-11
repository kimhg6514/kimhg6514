import sys
m,n = sys.stdin.readline().split()
m = int(m)
n = int(n)
if m > 10000:
    exit()
if n > 10000:
    exit()
max = int(0)
min = int(0)
if m> n :
    min = m
    for i in range(n) :
        if m%(i+1) == 0 and n%(i+1) ==0 :
            max = i+1    
    maxm = m/max
    maxn = n/max
    min = maxm*maxn*max
elif n> m :
    min = n
    for i in range(m) :
        if m%(i+1) == 0 and n%(i+1) ==0 :
            max = i+1
    maxm = m/max
    maxn = n/max
    min = int(maxm*maxn*max)
elif m ==n :
    min = m
    max = m
print(max)
print(int(min))