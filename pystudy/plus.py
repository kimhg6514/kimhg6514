import sys
num = int(sys.stdin.readline())
answer = [0 for _ in range(num)]
for i in range(num):
    col = int(sys.stdin.readline())
    plus = [0 for _ in range(col)]    
    plus = sys.stdin.readline().split()
    for y in range(col):
        answer[i] = int(answer[i])+int(plus[y])
for z in range(num):
    print(answer[z])
