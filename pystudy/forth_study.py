import sys
inputNum = int(input())
company = []
company2 = []
for i in range(inputNum):
    company.append(int(input()))
    company2.append(company[i])
company2.sort(reverse=True)
for x in company:
    print(company2.index(x)+1)
    


