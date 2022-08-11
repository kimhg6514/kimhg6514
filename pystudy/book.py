from sys import stdin
testCase = int(stdin.readline())
for i in range(testCase):
    N , M = map(int,stdin.readline().split())
    book = [0 for _ in range(N)]
    for z in range(M):
        a , b = map(int,stdin.readline().split())