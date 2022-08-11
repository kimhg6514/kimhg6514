import sys

num = input().split()
a = int(0)
for i in range(len(num)):
    a = a+int(num[i])

print(a ,"{:.2f}".format(a/(len(num))), sep = " ")