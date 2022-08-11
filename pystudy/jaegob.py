from sys import stdin
import math
number = int(stdin.readline())
check2 = False
num2 = int(0)
def issquare(n):
    return int(n**0.5)**2 ==n
def calculate(num) :
    x = int(1)
    checkpoint = False
    
    while checkpoint ==False :
        if issquare(num-(x**2))==True:
            checkpoint = True
        elif issquare(num-(x**2)-1) == True:
            return 2
        elif issquare(num-(x**2)-2) == True:
            return 3
        elif (x+1)**2 <num:
            x = x+1
        else :
            checkpoint = True
        
    return num-(x**2)
if issquare(number) == True:
    num2 = 1
else:
    while check2 ==False:
        i = calculate(number)
        print(i)
        num2 =num2+1
        if issquare(i) ==True:
            if i>0:
                num2 = num2+1
            check2 = True
        elif i>0:
        
            number = i
        else :
            
            check2 = True
print(num2)
