import sys
TestCase = int(input())

car = [0 for cars in range(TestCase)]



for i in range(TestCase) :
    price = int(input())
    options = int(input())
    
    for x in range(options) :
        opNum , opPri = input().split()
        opNum = int(opNum)
        opPri = int(opPri)
        price = price + (opNum * opPri)
    car[i] = price

for i in range(TestCase) :
    print(car[i])
        
