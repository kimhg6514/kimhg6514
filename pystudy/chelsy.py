testnum = int(input())

name2 =[0 for col in range(testnum)]

for i in range(testnum):
    personNum = int(input())
    person = [[0 for col in range(2)] for row in range(personNum)]
    name = [0 for col in range(personNum)]
    price = [0 for col in range(personNum)]
    for j in range(personNum):
        person[j] = list(map(str, input().split()))        
        price[j]= int(person[j][0])
        name[j] = person[j][1]
    tmpMax = max(price)
    MxIndex = price.index(tmpMax)
    name2[i] = name[MxIndex]

for x in range(testnum):
    print(name2[x])
    


