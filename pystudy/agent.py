start = list()
end = list()

start.append(input().split(':'))
end.append(input().split(':'))

if(len(start[0])==3):
   start[0]=str(0)+start[0]

print(start)