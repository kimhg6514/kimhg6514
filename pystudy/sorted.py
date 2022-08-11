from sys import stdin

number = int(stdin.readline())
n = [0]* 10001
for i in range(number):
   temp = int(stdin.readline())
   n[temp] = n[temp]+1
for i in range(10001):
    if n[i]> 0:
        for z in range(n[i]):
            print(i)