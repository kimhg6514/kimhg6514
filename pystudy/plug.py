import sys

n =  int(sys.stdin.readline())
plugs = int(0)
if(n<1 or n>500000):
   exit()
else :
    for i in range(n) :
        eachplug =  int(sys.stdin.readline())
        if(eachplug>1000):
           exit()
        else :
            plugs = plugs + eachplug

    plugs = plugs - (n-1)

    print(plugs)