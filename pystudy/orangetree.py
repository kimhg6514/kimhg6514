import sys


intX = int(1)
intY = int(1)
intR = int(3)
intTx = int(3)
intTy = int(4)

long = int(((intX-intTx)**2)+((intY-intTy)**2))
if(long<intR**2) :
    print("in")
elif(long==intR**2) :
    print("on")
else :
    print("out")




