import sys
checknum = [int(0) for i in range(5)]
 
checknum = sys.stdin.readline().split()
for i in range(len(checknum)):
    if int(checknum[i])<0 or int(checknum[i])>10:
        exit()
answer1 = int(0)
answer2 = int(0)
for i in range (len(checknum)):
    answer1 = answer1 + int(checknum[i])**2
answer2 = answer1%10
print(answer2)
