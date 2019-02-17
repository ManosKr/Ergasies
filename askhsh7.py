import random
def Cond(i,j,x,y,z,condition1):
    condition1 = False
    if i==0:
        if x[j]==0:
            condition1=True
    if i==1:
        if y[j]==0:
            condition1=True
    if i==2:
        if z[j]==0:
            condition1=True
    return condition1
def Check(N,k,i,x,y,z):
    N=0
    k=str
    for i in range(3):
        if x[i]==y[i]==z[i] and x[i]!=0:
            N=1
            k=x[i]
    for i in range(1):
        for i in range(2):
            if x[i]==x[i+1] and x[i]!=0:
                N=N+0.5
            else:
                N=0
        if N==1:
            k=x[i]
            break;
        for i in range(2):
            N=0
            if y[i]==y[i+1] and y[i]!=0:
                N=N+0.5
            else:
                N=0
        if N==1:
            k=x[i]
            break;
        for i in range(2):
            N=0
            if z[i]==z[i+1] and z[i]!=0:
                N=1
            else:
                N=0
            k=x[i]
    for i in range(2):
        if x[2*i]==y[1]==z[2-2*i] and x[2*i]!=0:
            N=1
            k=x[i]
    if N==1:
        print(k)
        print("Won the Game")
    return N
def tie(k,condition2,i,j,x,y,z):
    k=0
    condition2=False
    for i in range(3):
        for j in range(3):
            condition2=Cond(i,j,x,y,z,True)
            if condition2==False:
                k=k+1
    if k==9:
        print("You tied vs  random ai, FeelsBadMan")
def triliza(E,play1,play2,x,y,z,condition,n,l):
    E=True
    play1=0
    play2=0
    n=0
    for l in range(5):
        print ("Dwse suntetagmenes")
        while E==True:
            condition=True
            play1=int(input())
            play2=int(input())
            if 0<=play1 and play1<3 and 0<=play2 and play2<3:
                condition=Cond(play1,play2,x,y,z,False)
                if condition==True:
                    if play1==0:
                        x[play2]="O"
                    elif play1==1:
                        y[play2]="O"
                    elif play1==2:
                        z[play2]="O"
                    E=False
            else:
                print("Den mporeis na paikseis ekei")
        n=Check(0,0,0,x,y,z)
        E=True
        while E==True:
            if l==4:
                break;
            epilogh1=random.randint(0,2)
            epilogh2=random.randint(0,2)
            condition=Cond(epilogh1,epilogh2,x,y,z,False)
            if condition==True:
                if epilogh1==0:
                    x[epilogh2]="X"
                if epilogh1==1:
                    y[epilogh2]="X"
                if epilogh1==2:
                    z[epilogh2]="X"
                E=False
        E=True
        n=Check(0,0,0,x,y,z)
        print(x)
        print(y)
        print(z)

        if n==1:
            break;
    tie(0,True,0,0,x,y,z)
a=[0,0,0]
b=[0,0,0]
c=[0,0,0]
print (a)
print (b)
print (c)
triliza(True,0,0,a,b,c,True,0,0);
print("press a key to terminate")
terminate=input()
