from itertools import count
import sys


inputFunct = input()

splitInput2 = list(inputFunct)

splitInput = []

funcAnswer = ""

splitTrue = False

for x in range(len(splitInput2)) :
    if(splitTrue == False) :
        if(splitInput2[x]!="="):
            splitInput.append(splitInput2[x])
        else :
            splitTrue = True
    else :
        funcAnswer = funcAnswer + splitInput2[x]

calTrue = False

left = ""

answer =""

for i in range(len(splitInput)) :
    if(calTrue == True) :
       left = left + splitInput[i]
    else :
        if(splitInput[i] == '+') :
            calTrue = True     
            i = i+1   
        else :
            answer = answer + splitInput[i]
            i = i+1


if (calTrue == True) :
    IntLeft = -int(left)
else :
    answer = ""
    for j in range(len(splitInput)) :
        if(calTrue == True) :
          left = left + splitInput[j]
        else :
            if(splitInput[j] == '-') :
                calTrue = True     
                j = j+1   
            else :
                answer = answer + splitInput[j]
                j = j+1
    IntLeft = int(left)

answer2 = answer[:-1]
answer3 = (int(funcAnswer)+IntLeft)/int(answer2)
print(f"{answer3:.2f}")