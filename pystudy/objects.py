import sys
t = int(sys.stdin.readline())
if t<1 or t>100 :
    exit()
answer = []
for i in range(t):    
    v2,e2 = sys.stdin.readline().split()
    v2 = int(v2)
    e2 = int(e2)
    if v2<4 or v2>100:
        exit()
    if e2<4 or e2>100:
        exit()
    answer.append(e2-v2+2)
for i in range(t) :
    print(answer[i])


