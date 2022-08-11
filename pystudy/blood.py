import sys
parrent = ["AB" , "OO"]
parrent.sort()
blood = []
for i in range(2) :
    for j in range(2) :
        if(parrent[0][i:i+1] == parrent[1][j:j+1] or parrent[1][j:j+1] == "O" ) :
            blood.append(parrent[0][i:i+1])         
        elif(parrent[0][i:i+1] == "O") :
            blood.append(parrent[1][j:j+1]) 
        elif(parrent[0][i:i+1]+parrent[1][j:j+1] == "BA") :
            blood.append("AB")
        else :
            blood.append(parrent[0][i:i+1]+parrent[1][j:j+1])
blood = list(set(blood))
blood.sort()
for y in range(len(blood)) :
    print(blood[y], end = " ")

