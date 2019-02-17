def pick(f,kebap,newstring,a,b,count,c):
    if newstring=='zero':
        zero(f,newstring,count,a,b,c,kebap)
    if newstring=='one':
        one(f,newstring,count,a,b,c,kebap)
    if newstring=='two':
        two(f,newstring,count,a,b,c,kebap)
    if newstring=='three':
        three(f,newstring,count,a,b,c,kebap)
    if newstring=='four':
        four(f,newstring,count,a,b,c,kebap)
    if newstring=='five':
        five(f,newstring,count,a,b,c,kebap)
    if newstring=='six':
        six(f,newstring,count,a,b,c,kebap)
    if newstring=='seven':
        seven(f,newstring,count,a,b,c,kebap)
    if newstring=='eight':
        eight(f,newstring,count,a,b,c,kebap)
    if newstring=='nine':
        nine(f,newstring,count,a,b,c,kebap)

def diavasma(praxh,count,newstring):

    for i in range(count,25):

        if praxh[i]=="(":
            newstring=praxh[count:i]
            count=i+1
            break;
        if praxh[i]==")":
            newstring=praxh[count:i]
            count=i+1
            break;
    return newstring,count


def zero(f,newstring,count,a,b,c,kebap):
    if a==True:
        f[0]=0
        (newstring,count)=diavasma(praxh,count,newstring)
        kebap=newstring
        (newstring,count)=diavasma(praxh,count,newstring)
        a=False
    if b==True:
        if kebap=='plus':
            f[1]=f[0]+0
            print(f[1])
        if kebap=='minus':
            f[1]=f[0]-0
            print(f[1])
        if kebap=='times':
            f[1]=f[0]*0
            print(f[1])
        if kebap=='divided':
            print ("You can't deivide with 0")
    b=True
    if c==True:
        c=False
        pick(f,kebap,newstring,a,b,count,c)



def one(f,newstring,count,a,b,c,kebap):
    if a==True:
        f[0]=1
        (newstring,count)=diavasma(praxh,count,newstring)
        kebap=newstring
        (newstring,count)=diavasma(praxh,count,newstring)
        a=False
    if b==True:
        if kebap=='plus':
            f[1]=f[0]+1
            print(f[1])
        if kebap=='minus':
            f[1]=f[0]-1
            print(f[1])
        if kebap=='times':
            f[1]=f[0]*1
            print(f[1])
        if kebap=='divided':
            f[1]=f[0]//1
            print(f[1])
    b=True
    if c==True:
        c=False
        pick(f,kebap,newstring,a,b,count,c)



def two(f,newstring,count,a,b,c,kebap):
    if a==True:
        f[0]=2
        (newstring,count)=diavasma(praxh,count,newstring)
        kebap=newstring
        (newstring,count)=diavasma(praxh,count,newstring)
        a=False
    if b==True:
        if kebap=='plus':
            f[1]=f[0]+2
            print(f[1])
        if kebap=='minus':
            f[1]=f[0]-2
            print(f[1])
        if kebap=='times':
            f[1]=f[0]*2
            print(f[1])
        if kebap=='divided':
            f[1]=f[0]//2
            print(f[1])
    b=True
    if c==True:
        c=False
        pick(f,kebap,newstring,a,b,count,c)



def three(f,newstring,count,a,b,c,kebap):
    if a==True:
        f[0]=3
        (newstring,count)=diavasma(praxh,count,newstring)
        kebap=newstring
        (newstring,count)=diavasma(praxh,count,newstring)
        a=False
    if b==True:
        if kebap=='plus':
            f[1]=f[0]+3
            print(f[1])
        if kebap=='minus':
            f[1]=f[0]-3
            print(f[1])
        if kebap=='times':
            f[1]=f[0]*3
            print(f[1])
        if kebap=='divided':
            f[1]=f[0]//3
            print(f[1])
    b=True
    if c==True:
        c=False
        pick(f,kebap,newstring,a,b,count,c)



def four(f,newstring,count,a,b,c,kebap):
    if a==True:
        f[0]=4
        (newstring,count)=diavasma(praxh,count,newstring)
        kebab=newstring
        (newstring,count)=diavasma(praxh,count,newstring)
        a=False
    if b==True:
        if kebap=='plus':
            f[1]=f[0]+4
            print(f[1])
        if kebap=='minus':
            f[1]=f[0]-4
            print(f[1])
        if kebap=='times':
            f[1]=f[0]*4
            print(f[1])
        if kebap=='divided':
            f[1]=f[0]//4
            print(f[1])
    b=True
    if c==True:
        c=False
        pick(f,kebap,newstring,a,b,count,c)


def five(f,newstring,count,a,b,c,kebap):
    if a==True:
        f[0]=5
        (newstring,count)=diavasma(praxh,count,newstring)
        kebap=newstring
        (newstring,count)=diavasma(praxh,count,newstring)
        a=False
    if b==True:
        if kebap=='plus':
            f[1]=f[0]+5
            print(f[1])
        if kebap=='minus':
            f[1]=f[0]-5
            print(f[1])
        if kebap=='times':
            f[1]=f[0]*5
            print(f[1])
        if kebap=='divided':
            f[1]=f[0]//5
            print(f[1])
    b=True
    if c==True:
        c=False
        pick(f,kebap,newstring,a,b,count,c)



def six(f,newstring,count,a,b):
    if a==True:
        f[0]=6
        (newstring,count)=diavasma(praxh,count,newstring)
        kebap=newstring
        (newstring,count)=diavasma(praxh,count,newstring)
        a=False
    if b==True:
        if kebap=='plus':
            f[1]=f[0]+6
            print(f[1])
        if kebap=='minus':
            f[1]=f[0]-6
            print(f[1])
        if kebap=='times':
            f[1]=f[0]*6
            print(f[1])
        if kebap=='divided':
            f[1]=f[0]//6
            print(f[1])
    b=True
    if c==True:
        c=False
        pick(f,kebap,newstring,a,b,count,c)



def seven(f,newstring,count,a,b,c):
    if a==True:
        f[0]=7
        (newstring,count)=diavasma(praxh,count,newstring)
        kebap=newstring
        (newstring,count)=diavasma(praxh,count,newstring)
        a=False
    if b==True:
        if kebap=='plus':
            f[1]=f[0]+7
            print(f[1])
        if kebap=='minus':
            f[1]=f[0]-7
            print(f[1])
        if kebap=='times':
            f[1]=f[0]*7
            print(f[1])
        if kebap=='divided':
            f[1]=f[0]//7
            print(f[1])
    b=True
    if c==True:
        c=False
        pick(f,kebap,newstring,a,b,count,c)



def eight(f,newstring,count,a,b,c,kebap):
    if a==True:
        f[0]=8
        (newstring,count)=diavasma(praxh,count,newstring)
        kebap=newstring
        (newstring,count)=diavasma(praxh,count,newstring)
        a=False
    if b==True:
        if kebap=='plus':
            f[1]=f[0]+8
            print(f[1])
        if kebap=='minus':
            f[1]=f[0]-8
            print(f[1])
        if kebap=='times':
            f[1]=f[0]*8
            print(f[1])
        if kebap=='divided':
            f[1]=f[0]//8
            print(f[1])
    b=True
    if c==True:
        c=False
        pick(f,kebap,newstring,a,b,count,c)



def nine(f,newstring,count,a,b,c,kebap):
    if a==True:
        f[0]=9
        (newstring,count)=diavasma(praxh,count,newstring)
        kebap=newstring
        (newstring,count)=diavasma(praxh,count,newstring)
        a=False

    if b==True:
        if kebap=='plus':
            f[1]=f[0]+9
            print(f[1])
        if kebap=='minus':
            f[1]=f[0]-9
            print(f[1])
        if kebap=='times':
            f[1]=f[0]*9
            print(f[1])
        if kebap=='divided':
            f[1]=f[0]//9
            print(f[1])
    b=True
    if c==True:
        c=False
        pick(f,kebap,newstring,a,b,count,c)



praxh=str(input())
newstring=[]
count=0
f=[0,0]
a=True
b=False
c=True
kebap="valhala"
(newstring,count)=diavasma(praxh,count,newstring)
pick(f,kebap,newstring,a,b,count,c)
print("press a key to terminate")
terminate=input()
