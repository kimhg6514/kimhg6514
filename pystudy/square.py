from difflib import SequenceMatcher


import math
m =int(input())
n = int(input())

if m> n:
    exit()
if m>10000 :
    exit()
if n>10000 :
    exit()

min = int(0)

checkpoint = 0
value = int(0)

for i in range(n-m+1) :
    if m%math.sqrt(m) == int(0) :
        
        value = value + m
        if checkpoint == 0 :
            min = m
            checkpoint = 1
    m = m+1
if value == 0 :
    print("-1")
else:
    print(value)
    print(min)