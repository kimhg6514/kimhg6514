import sys
a , b = sys.stdin.readline().split()
e = float(1/int(a))
c = (float(b)+(e))
d= c%1
f = float(0)
for i in range(int(a)) :   
    d = (d + (e*i)) % 1
    f = f+d 
print(f"{f:.4f}")

