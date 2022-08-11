import sys
num = int(sys.stdin.readline())
cars = [0 for i in range(5)]
cars = sys.stdin.readline().split()
alert = int(0)
for i in range(5):
    if int(int(cars[i])==num):
        alert = alert+1
print(alert)