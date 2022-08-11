num = int(9)
a = [0 for j  in range(num)]

for i in range(num):
    a[i] = int(input())

tmpMax = max(a)
MaxInd = int(a.index(tmpMax))
print(tmpMax)
print(MaxInd+1)
