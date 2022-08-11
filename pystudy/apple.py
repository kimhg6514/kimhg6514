import sys

n = int(input())

left = int(0)

for i in range(n) :
    student , apple = input().split()
    Istudent = int(student)
    Iapple = int(apple)
    left = left + (Iapple % Istudent)
print(left)
    