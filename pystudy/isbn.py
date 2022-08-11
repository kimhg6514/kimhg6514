import sys
m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
have = int(91)
answer = have+ m+n*3+k

print("The 1-3-sum is "+str(answer))