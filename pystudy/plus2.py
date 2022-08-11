import sys

n , k = map(int,sys.stdin.readline().split())
check = 0
if n>10**9:
    exit()
if k>50:
    exit()
values = int(0)
sum = ((n+1)*n)/2



print(sum)