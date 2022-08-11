import sys
array1 = [[0 for col in range(11)] for row in range(10)]
array2  = []
c = 0
for i in range(int(10)) :
    for j in range(int(10)) :
        if(i == 0 or i == 0 or j == 0 or j == 9 ) :
            array2.append("1")
        else :
            array2.append("0")
    print(array2[j])
    c = array2[j]  
    array1[i][j] = c    
    array2 = [0 for x in range(10)]
print(array1)



