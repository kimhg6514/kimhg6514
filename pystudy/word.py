word = list(input())
if word[0] ==' ':
    if word[len(word)-1] == ' ':
        print(word.count(' ')-1)
    else :
        print(word.count(' '))
elif word[len(word)-1] == ' ':
    print(word.count(' '))
elif word[len(word)-1] == ' ' and word[0] ==' ':
    print(word.count(' ')-1)
elif word.count(' ') == 1 and len(word) == 1:
    print('0')
else :
    print(word.count(' ')+1)
