from sys import stdin

num = int(stdin.readline())
command = [[0 for i in range(2)] for z in range(num)]
print(command)
z = int(0)
stack = [0 for i in range(num)]
for i in range(num):
   command[i] = stdin.readline().split()
  
for i in range(num):
    if command[i][0] =="push":
        stack[z] = command[i][1]  
        z = z+1
    elif command[i][0] == "pop":
        if z == 0:
            if stack[z] == int(0):
                print("-1")
            else:
                print(stack[z])
                stack[z] = 0
        else :
            if stack[z-1] == int(0):
                print("-1")
            else:
                print(stack[z-1])
                stack[z-1] = 0
            z = z-1
    elif command[i][0] == "size":
        print(num-int(stack.count(0)))
    elif command[i][0] == "empty" :
        if stack.count(0) == num:
            print("1")
        else :
            print("0")
    elif command[i][0] == "top":
        if stack[z-1] ==int(0):
            print("-1")
        else :
            print(stack[z-1])
