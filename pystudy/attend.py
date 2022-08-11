import sys
n = int(input())

num = input().split()
for i in range(len(num)) :
    print(num[len(num)-i-1], end =" ")

