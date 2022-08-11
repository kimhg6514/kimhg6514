from sys import stdin
number = int(stdin.readline())
runner = list()
bestrun = list()
for i in range(number):
    runner.append(int(stdin.readline()))
def best(num):
    number2 = num-1
    number3 = num
    while number2 >=0:
        if runner[num]>runner[number2]:
            number3 = number3 -1
        number2 = number2-1
        bestrun.append(number3+1)
    return bestrun
best(number-1)
print(bestrun)


