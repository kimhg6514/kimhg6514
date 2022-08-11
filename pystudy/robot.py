from pickle import FALSE, TRUE
import sys
n , l , r = input().split()
intN = int(n)
intL = int(l)
intR = int(r)
move = int(0)
Ffirst = int(0)
Llast = int(0)
TTrue = FALSE
cnt = int(0)
finalcheck = int(0)
sensor = list(input().split())
if(2*intR*intN<intL) :
    print(-1)
else :    
    for i in range(intN-1) :
        if(int(sensor[i])>2*intR*(i)+intR  and TTrue == FALSE):           
            Ffirst = i
            TTrue = TRUE
        if(int(sensor[i+1])<2*intR*(i)+int(sensor[i]) ):           
            cnt = i           
if(cnt == 0) :    
    if(Ffirst ==0) :
        if(TTrue == TRUE) :
            move = 2*int(sensor[0])-intR
        else :
            for z in range(intN-1) :
                if(int(sensor[z+1])>(int(sensor[z])+2*intR)) :
                    move = int(sensor[z+1])-2*intR 
    else :
        move = int(sensor[cnt])+(2*intR*(Ffirst+1)-int(sensor[Ffirst]))
else :
    move = (2*(int(sensor[cnt+1])-(2*intR)))-(2*intR*(Ffirst)+intR)
print(Ffirst)
print(cnt)
print(int(move))
