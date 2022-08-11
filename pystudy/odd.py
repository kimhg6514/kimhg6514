import sys
num = int(7)

number =[0 for i in range(num) ]

odd = []

oddnum = int(0)

value = int(0)

for i in range(num) :
    
    number[i] = int(input())
    if number[i]>100:
        exit()

for i in range(num) :
    if number[i]%2 == 1 :
        odd.append(number[i])
        oddnum = oddnum+1
if oddnum == 0:
    print("-1")
else :

    for i in range(oddnum) :
        value = value + odd[i]

    tmpmin = min(odd)
    print(value)
    print(tmpmin)