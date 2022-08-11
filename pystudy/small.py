size , num = input().split()
intSize = int(size)
intNum = int(num)

array1 = [0 for col in range(intSize)]

array1 = list(map(str, input().split()))  

for x in range(intSize):
    if(int(array1[x])<intNum) :
        print(array1[x], end = " ")