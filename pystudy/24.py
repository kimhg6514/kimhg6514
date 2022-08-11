import sys
start = [0 for i in range(3)]
now = [0 for i in range(3)]
left = [0 for i in range(3)]
now= sys.stdin.readline().split(":")
start = sys.stdin.readline().split(":")
start2 = start[0]+start[1]+start[2]
now2 = now[0]+now[1]+now[2]
if int(start2)-int(now2)<0 :
    start[0] = int(start[0])+int(24)
left[2] = int(start[2])-int(now[2])
if left[2]<0 :
    left[2] = left[2]+int(60)
    start[1] = int(start[1])-int(1)
left[1] = int(start[1])-int(now[1])
if left[1]<0 :
    left[1] = left[1]+int(60)
    start[0] = int(start[0])-int(1)
left[0] = int(start[0])-int(now[0])
if left[0]<0 :
    left[0] = left[0]+int(24)
for i in range(3):
    if int(left[i]<10) :
        left[i] = "0"+str(left[i])
print(left[0],left[1],left[2], sep=":")
    