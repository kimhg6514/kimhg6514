from re import A
import sys
berry  = ["4","5","2","3","1"]
Ssize = int(3)
a = int(0)
b = int(0)
i = int(0)
while a < 3 : 
    if(a ==0) :
        if(int(berry[i])<Ssize) :
         print(berry[i], end= " ")
    elif(a ==1) :
        if(int(berry[i])==Ssize) :
         print(berry[i], end= " ")
    elif(a ==2) :        
        if(int(berry[i])>Ssize) :
         print(berry[i], end= " ")    
    i = i+1
    if(i==(len(berry))) :        
        if(a !=2) :         
          a = a+1
          i = int(0)
        else :
            break
        
        
          
    




