def isprime(x):
   for i in range(2,x-1):
      if x%i == 0:
         return 1
   return 0
a , b = map(int,input().split())

for i in range(a,b+1):
    if isprime(i) == 0:
        print(i)