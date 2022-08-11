from sys import stdin

num = int(stdin.readline())
numarray = [0 for i in range(2001)]
temp = list(map(int, stdin.readline().split()))

for z in range(num):
    numarray[temp[z]+1000] = 1

for x in range(2001):
    if numarray[x] == 1:
        print(x-1000 , end = " ")
