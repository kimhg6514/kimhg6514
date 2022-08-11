import sys
testCase = int(sys.stdin.readline())
a = [[0 for i in range(2)] for i in range(testCase)]
for i in range(testCase):
    a[i]=sys.stdin.readline().split()   
for i in range(testCase):
    print("Case ",i+1,": ",int(a[i][0])+int(a[i][1]),sep="")