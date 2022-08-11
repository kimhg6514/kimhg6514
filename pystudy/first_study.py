from random import randint, random
import sys

callcount = int(input())

callList3 = input().split()
callList = []


for i in range(callcount) :
    callList.append(callList3[i])

callList2 = list(map(int , callList))

callList2.sort()

print(callList2)
