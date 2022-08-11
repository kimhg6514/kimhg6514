import sys
a , b = sys.stdin.readline().split()
inta = int(a)
f = float(0)
f = (inta*(inta+1)/2 * ((float(b)+1/int(a))%1))
print(f"{f:.4f}")