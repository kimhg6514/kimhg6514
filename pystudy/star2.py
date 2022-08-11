from re import L
import sys
row = int(sys.stdin.readline())
for i in range(row):
    for y in range(i):
        print(" ",end="")
    for x in range(row-i):
        print("*",end="")
    print("")