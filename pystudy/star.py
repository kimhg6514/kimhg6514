num = int(input())

for i in range(num):
    for j in range(num*2):
        if((i+1)%2 == 1):
            if((j+1)%2 == 1):
                print("*", end="")
            else:
                print(" ",end="")
        else:
            if((j+1)%2 == 0):
                print("*", end="")
            else:
                print(" ",end="")
    print("")