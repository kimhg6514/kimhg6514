import sys
n = int(input())
a= int(0)
b= int(1)
c = int(0)
if(n==0):
    c=0
elif(n==1):
    c=1
elif(n==2):
    c=1
else :
    for i in range(n-1) :
        c = a+b
        a = b
        b = c
print(c)