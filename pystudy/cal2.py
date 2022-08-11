import sys

TrueEnd = False

Answer = []

n = int(0)

while TrueEnd == False :

    a , b = input().split()
    intA = int(a)
    intB = int(b)
    if(intA == 0 and intB == 0 ):

        TrueEnd = True
    else :
        Answer.append(intA+intB)
        n=n+1

for i in range(n) :
    print(Answer[i])
