import sys
num = int(input())
yearNum = []
cnt = int(0)
for i in range(num) :
    yearNum.append(input())
for i in range(len(yearNum)) :
    yearMon = yearNum[i].replace(" ","").strip()
    yearMon1 =yearMon[::-1]
    if(yearMon1 == yearMon) :
        cnt = cnt+int(1)
print(cnt)


    
