

number = int(input())

birthday = [[0 for col in range(4)] for row in range(number)]
name = [0 for col in range(number)]
date = [0 for col in range(number)]

for i in range(number):
    birthday[i] = list(map(str, input().split()))
    

for x in range(number) :
    name[x] = str(birthday[x][0])
    if(int(birthday[x][2])<10):
        birthday[x][2] = "0"+birthday[x][2]
    if(int(birthday[x][1])<10):
        birthday[x][1] = "0"+birthday[x][1]
    date[x] = int(birthday[x][3]+birthday[x][2]+birthday[x][1])

Mxtmp = max(date)
MxIndex = date.index(Mxtmp)

MiTmp = min(date)
MiIndex = date.index(MiTmp)

print(name[MxIndex])
print(name[MiIndex])

  