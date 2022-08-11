import sys
import math
m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
if m>10000 or m>n :
    exit()
numlist = list(map(int, range(m,n+1)))
checkpoint = False
answer1 = int(0)
answer2 = int(0)
def prime_number(n) :
    for i in range(2, int(math.sqrt(n))+1):
        if n%i ==0 :
            return False
    return True

for i in range(len(numlist)) :
    b = int(numlist[i])
    if b != 1:
        a = prime_number(b)
        if a == True:
            answer1 = answer1+b
            if checkpoint ==False:
                answer2 = answer2 + b
                checkpoint = True
if answer1 == 0:
    print(-1)
else :
    print(answer1)
    print(answer2)