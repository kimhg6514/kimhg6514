import sys
n = int(input())

cal = [0 for i in range(n)]

for x in range(n):
    a , b = input().split()
    intA = int(a)
    intB = int(b)
    cal[x] = intA+intB

for y in range(n):
    print(cal[y])