from sys import stdin


def ispel(x):
   pellist = list(x)
   checkpel = False
   i = int(0)
   while checkpel ==False:
      if i<len(pellist)/2:
         if pellist[i] != pellist[len(pellist)-i-1]:
            return 1
         else :            
            i = i+1            
      else :
         return 0

def isprime(x):
   for i in range(2,x-1):
      if x%i == 0:
         return 1
   return 0

num = int(input())
if num == 1:
   num = num+1

while 1 ==1:
   if ispel(str(num))==0 and isprime(num) == 0:
      print(num)
      exit()
   else:
      num = num+1