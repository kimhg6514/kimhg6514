import sys
n , k = sys.stdin.readline().split()
n = int(n)
k = int(k)
if n<1 or n>10000 :
    exit()
if k<1 or k>n:
    exit()
m = int(0)
i = int(1)
while m < k :
    if i>n:
        print("0")
        exit()
    if n%i ==0 :
        m = m+1
    if m == k:
        print(i)
    i = i+1

