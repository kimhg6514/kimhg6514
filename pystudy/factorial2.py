import sys
import math
i = int(input())
b = int(1)
c = int(0)
a = int(3)
d = int(0)
if(i==1):
    print(0)
elif(i ==2) :
    print(1)
else :
    for x in range(i-2) :
        d = int((a-1)*(b+c))
        c = b
        b = d % 1000000007
        a=a+1
   
    print(b)
    