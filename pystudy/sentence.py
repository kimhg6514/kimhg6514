point = list(input())
points = 0.0

if point[0] =="A":
    points = points +4.0
elif point[0] =="B":
    points = points +3.0
elif point[0] =="C":
    points = points +2.0
elif point[0] =="D":
    points = points +1.0
elif point[0] =="F":
    print(points)
    exit()
if point[1] =="+":
    points = points +0.3
elif point[1] =="0":
    points = points +0.0
elif point[1] =="-":
    points = points -0.3
print(points)