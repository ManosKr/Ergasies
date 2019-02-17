import string
string.ascii_lowercase
string.ascii_uppercase
text=str(input())
len=len(text)
grammata=list(string.ascii_lowercase)
kefalaia=list(string.ascii_uppercase)
statistika = [[0  for i in range(3)]for j in range(26)]


for i in range(26):
    statistika[i][1]=kefalaia[i]
    statistika[i][0]=grammata[i]


for i in range(len):
    for j in range(26):
        if text[i]==grammata[j] or text[i]==kefalaia[j]:
            statistika[j][2]=statistika[j][2]+1


statistika = sorted(statistika, key=lambda x: x[2], reverse=True)


newtext=[0 for i in range(len)]
for i in range(len):
    newtext[i]=text[i]


for i in range(len):
    for j in range(26):
        if text[i]==statistika[j][0]:
            newtext[i]=statistika[25-j][1]

print(newtext)
print("press a key to terminate")
terminate=input()
