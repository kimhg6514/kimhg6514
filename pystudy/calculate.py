number2 = input()

if int(number2)<10 :
    number2 = "0"+number2
number = number2
i = int(1)
while 1 ==1:
    numberlist = list(number)
    temp = int(numberlist[0])+int(numberlist[1])
    templist = list(str(temp))
    temp = numberlist[1]+templist[len(templist)-1]
    if temp !=number2 :
        i = i+1
        number =temp
    else :
        print(i)
        exit()


