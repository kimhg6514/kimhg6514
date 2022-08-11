num = int(input())
answer = [0 for i in range(num)]
point = [0 for i in range(num)]
answer = input().split()
fullpoint = int(0)

for i in range(num):
    if(answer[i] == "1") :
        if(i>0):
            if(int(point[i-1])>0):
                point[i] = int(point[i-1]+1)
            else : 
                point[i] = 1
        else :
            point[i] = 1

for i in range(num) :
    fullpoint = fullpoint + int(point[i])

print(fullpoint)
