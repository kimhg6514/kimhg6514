num = int(input())
triangle = [0 for _ in range(3)]
answer = []

for i in range(num):
    triangle=list(map(int,input().split()))
    triangle.sort()
    if (triangle[0]**2)+(triangle[1]**2) == (triangle[2]**2):
        answer.append("yes")
    else:
        answer.append("no")

for i in range(num):
    print("Scenario #",i+1,":",sep="")
    print(answer[i])