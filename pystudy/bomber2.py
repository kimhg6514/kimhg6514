import sys
import copy
row,col,number = map(int,sys.stdin.readline().split())
maplist =  [list(input())for i in range(row)]
maplist2 = copy.deepcopy(maplist)

for i in range(row) :
    for x in range(col):
            if maplist2[i][x] == "O" :
                maplist2[i][x] = "." 
            else :
                maplist2[i][x] = "O"  

if number %4 == 1 :
    maplist = maplist

elif number%2==0 :
    for i in range(row) :
        for x in range(col) :
            maplist[i][x] = "O"  
else :
    maplist = copy.deepcopy(maplist2)    
    for i in range(row) :
        for x in range(col):
           if maplist2[i][x] == "."  :
            if i == 0 and x == 0 :
                maplist[i+1][x]= "." 
                maplist[i][x+1]= "."
            elif i == 0 and  x==col-1  :
                maplist[i+1][x]= "." 
                maplist[i][x-1]= "." 
            elif i == 0 and x > 0 and x < col-1  :
                maplist[i+1][x]= "." 
                maplist[i][x+1]= "." 
                maplist[i][x-1]= "." 
            elif i == row-1 and x == 0 :
                maplist[i-1][x]= "." 
                maplist[i][x+1]= "."
            elif i == row-1 and x == col-1 :
                maplist[i-1][x]= "." 
                maplist[i][x-1]= "."
            elif i == row-1 and x < col-1 and x >0 :
                maplist[i-1][x]= "." 
                maplist[i][x+1]= "."
                maplist[i][x-1]= "."
            elif (i>0 and i < row-1) and x == 0:
                maplist[i+1][x]= "." 
                maplist[i-1][x]= "." 
                maplist[i][x+1]= "." 
            elif (i>0 and i<row-1) and x == col-1:
                maplist[i+1][x]= "." 
                maplist[i+1][x]= "." 
                maplist[i][x-1]= "." 
            elif i>0 and i< row-1 and x>0 and x<col-1:
                maplist[i-1][x]= "." 
                maplist[i][x-1]= "." 
                maplist[i+1][x]= "." 
                maplist[i][x+1]= "." 


for i in range(row):
    for x in range(col):
        print(maplist[i][x],end="")
    print()