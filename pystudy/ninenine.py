inputNum = int(input())
if inputNum<1 or inputNum>10 :
    exit()
for i in range(9):
    print(inputNum," * ",i+1," = ",(inputNum*(i+1)),sep="")