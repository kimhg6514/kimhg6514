import sys

num = input()

intnum = int(num)

for i in range(intnum) :
    if((i+1)%10==0) :
        if((i+1)%3==0):
            print("X" , end =" ")
        else :
            print(i+1, end = " ")
    else :
        if(((i+1)%10)%3 == 0):
            print("X" , end =" ")
        else:
            print(i+1, end = " ")