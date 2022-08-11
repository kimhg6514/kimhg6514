import sys

num = int(input())
boxA = int(10)
boxB = int(5)
boxC = int(3)
boxD = int(1)
intA = 0
intB = 0
intC = 0
intD = 0

for i in range(num+1) :
    if(num- (boxA*i) >=0 ) :
        intA=i
    else :
        break


num = num-(boxA*intA)

for i in range(num+1) :
    if(num- (boxB*i) >=0 ) :
        intB=i
    else :
        break

    
num = num-(boxB*intB)

for i in range(num+1) :
    if(num- (boxC*i) >=0 ) :
        intC=i
    else :
        break

num = num-(boxC*intC)

for i in range(num+1) :
    if(num- (boxD*i) >=0 ) :
        intD=i
    else :
        break


print(intA+intB+intC+intD)