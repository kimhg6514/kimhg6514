from sys import stdin
colors = [0 for i in range(5)]
numbers = [0 for i in range(5)]
score = int(0)
for i in range(5):
   colors[i] , numbers[i] = stdin.readline().split()

if len(set(colors)) == 1 and int(numbers[4]) == int(numbers[3])+1 == int(numbers[2]) +2 == int(numbers[1])+3 == int(numbers[0]) +4 :
    score = 900 + int(numbers[4])
print(score)
