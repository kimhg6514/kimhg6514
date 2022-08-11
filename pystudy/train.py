from sys import stdin

train = int(0)
max = int(0)

for i in range(4):
    Out , In = map(int, stdin.readline().split())
    train = train - Out
    train = train + In
    if max< train:
        max = train
print(max)