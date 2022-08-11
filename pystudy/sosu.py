import sys
import math
num = int(sys.stdin.readline())
numlist = list(map(int,sys.stdin.readline().split()))
answer = int(0)
def prime_number(n) :
    for i in range(2, int(math.sqrt(n))+1):
        if n%i ==0 :
            return False
    return True

for i in range(num) :
    b = numlist[i]    
    b = int(b)
    if b != 1:
        a = prime_number(b)
        if a == True:
            answer = answer+1

print(answer)