import sys

testcase = int(input())
candies = [0 for i in range(testcase)]
left = [0 for i in range(testcase)]
for i in range(testcase) :
    candy , brothers = input().split()
    candy = int(candy)
    brothers = int(brothers)

    if(candy<1) :
        print("")
    else :
        if(brothers>1000):
            break
        else:
            candies[i] = candy//brothers
            left[i] = candy%brothers




for i in range(testcase):
    print("You get "+str(candies[i])+" piece(s) and your dad gets "+str(left[i])+" piece(s)." )

