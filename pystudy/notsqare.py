from sys import stdin
numA , numB = map(int,stdin.readline().split())
z = int(0)

def isjaegobnono(x) :
    for i in range(int(x//2)):
        if x%((i+2)**2) == 0:
            return 0
    return 1

for i in range(numB-numA+1):
    if isjaegobnono(numA) ==1:
        z = z+1
    numA = numA+1
print(z)