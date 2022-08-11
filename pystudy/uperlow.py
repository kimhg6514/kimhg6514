
sentence = list(input())
sentence2 = []

for i in range(len(sentence)):
    if sentence[i].isupper() == True:
        sentence2.append(sentence[i].lower())
    else:
        sentence2.append(sentence[i].upper())
for i in range(len(sentence2)):
    print(sentence2[i], end="")