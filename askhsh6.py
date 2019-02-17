import random

def karoto(Matrix,vomvax,vomvay,x,y):
    a=True
    x=x-1
    y=y-1
    while a==True:
        vomvax=random.randint(0,x)
        vomvay=random.randint(0,y)
        if Matrix[vomvay][vomvax]==0:
            a=False
    return (vomvax,vomvay)





print("Dwse diastaseis gia ton narkalieuth")
print("Sthles: ")
x=int(input())
print("Grammes: ")
y=int(input())
Matrix = [[0 for i in range(x)] for j in range(y)]




a=True
print("Poses vomves na exei o xarths")
while (a==True):
    vomves=int(input())
    if vomves>(x*y):
        print("Den mporeis na exeis toses vomves")
        vovmes=int(input())
    else:
        a=False
Kappa = [[0 for i in range(2)] for j in range(vomves)]




vomvax=0
vomvay=0
for i in range(vomves):
    (vomvax,vomvay)=karoto(Matrix,0,0,x,y)
    Kappa[i][0]=vomvax
    Kappa[i][1]=vomvay
    Matrix[vomvay][vomvax]=9


for i in range(vomves):
        x1=Kappa[i][0]
        y1=Kappa[i][1]
        if x1!=0 and x1!=x-1:
            if y1!=0 and y1!=y-1:
                Matrix[y1-1][x1-1]=Matrix[y1-1][x1-1]+1
                Matrix[y1-1][x1]=Matrix[y1-1][x1]+1
                Matrix[y1-1][x1+1]=Matrix[y1-1][x1+1]+1
                Matrix[y1][x1+1]=Matrix[y1][x1+1]+1
                Matrix[y1+1][x1+1]=Matrix[y1+1][x1+1]+1
                Matrix[y1+1][x1]=Matrix[y1+1][x1]+1
                Matrix[y1+1][x1-1]=Matrix[y1+1][x1-1]+1
                Matrix[y1][x1-1]=Matrix[y1][x1-1]+1
            elif y1==0:
                Matrix[y1][x1+1]=Matrix[y1][x1+1]+1
                Matrix[y1+1][x1+1]=Matrix[y1+1][x1+1]+1
                Matrix[y1+1][x1]=Matrix[y1+1][x1]+1
                Matrix[y1+1][x1-1]=Matrix[y1+1][x1-1]+1
                Matrix[y1][x1-1]=Matrix[y1][x1-1]+1
            else:
                Matrix[y1-1][x1-1]=Matrix[y1-1][x1-1]+1
                Matrix[y1-1][x1]=Matrix[y1-1][x1]+1
                Matrix[y1-1][x1+1]=Matrix[y1-1][x1+1]+1
                Matrix[y1][x1+1]=Matrix[y1][x1+1]+1
                Matrix[y1][x1-1]=Matrix[y1][x1-1]+1
        elif x1==0:
            if y1!=0 and y1!=y-1:
                Matrix[y1-1][x1]=Matrix[y1-1][x1]+1
                Matrix[y1-1][x1+1]=Matrix[y1-1][x1+1]+1
                Matrix[y1][x1+1]=Matrix[y1][x1+1]+1
                Matrix[y1+1][x1+1]=Matrix[y1+1][x1+1]+1
                Matrix[y1+1][x1]=Matrix[y1+1][x1]+1
            elif y1==0:
                Matrix[y1][x1+1]=Matrix[y1][x1+1]+1
                Matrix[y1+1][x1+1]=Matrix[y1+1][x1+1]+1
                Matrix[y1+1][x1]=Matrix[y1+1][x1]+1

            else:
                Matrix[y1-1][x1]=Matrix[y1-1][x1]+1
                Matrix[y1-1][x1+1]=Matrix[y1-1][x1+1]+1
                Matrix[y1][x1+1]=Matrix[y1][x1+1]+1
        else:
            if y1!=0 and y1!=y-1:
                Matrix[y1-1][x1-1]=Matrix[y1-1][x1-1]+1
                Matrix[y1-1][x1]=Matrix[y1-1][x1]+1
                Matrix[y1+1][x1]=Matrix[y1+1][x1]+1
                Matrix[y1+1][x1-1]=Matrix[y1+1][x1-1]+1
                Matrix[y1][x1-1]=Matrix[y1][x1-1]+1
            elif y1==0:
                Matrix[y1][x1-1]=Matrix[y1][x1-1]+1
                Matrix[y1+1][x1-1]=Matrix[y1+1][x1-1]+1
                Matrix[y1+1][x1]=Matrix[y1+1][x1]+1

            else:
                Matrix[y1-1][x1]=Matrix[y1-1][x1]+1
                Matrix[y1-1][x1-1]=Matrix[y1-1][x1-1]+1
                Matrix[y1][x1-1]=Matrix[y1][x1-1]+1

for i in range(x):
    for j in range(y):
        if Matrix[j][i]>8:
            Matrix[j][i]="B"

for i in range(y):
    print (Matrix[i])
print("press a key to terminate")
terminate=input()
