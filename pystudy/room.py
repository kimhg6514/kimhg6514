num = int(input())
room = [list(0 for i in range(num))for z in range(num)]
horizonscore = int(0)
verticalscore = int(0)

for i in range(num):
    room[i]=list(input())
    for y in range(num-1):
        if room[i][y] =='.' and room[i][y+1] =='.': 
            if y!=0 and  room[i][y-1] != '.':          
                horizonscore = horizonscore+1
            elif y == 0:
                horizonscore = horizonscore+1

for i in range(num):
    for x in range(num-1):
        if room[x][i] == '.' and room[x+1][i] == '.':
            if x!=0 and  room[x-1][i] != '.':  
                verticalscore = verticalscore +1
            elif x==0:
                verticalscore = verticalscore +1
            

print(horizonscore,verticalscore, sep=" ")

   
