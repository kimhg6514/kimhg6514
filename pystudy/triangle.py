import sys

max = int(input())

chk = int(0)
chk2 = int(0)

for length in range(max+1) :
    for a in range(length) :  
        if a != 0:      
            for b in range(length-a) :
                if b!= 0:
                    if ((b*b)+(a*a)) == (length-(a+b))**2 : 
                        chk=chk+1
                        

    if chk == 2 :
        
        chk2 = chk2+1
        
    chk = 0

print(chk2)
