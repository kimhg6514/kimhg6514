from sys import stdin
num = int(stdin.readline())
criminal = [(0 for _ in range(num)) for z in range(num)] 
for i in range(num):
    criminal[i] = list(map(int,stdin.readline().split()))
print(criminal)
