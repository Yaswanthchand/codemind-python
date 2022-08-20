def selfdiv(a):
    t=a
    flag=0
    while t>0:
        r=t%10
        if r==0:
            flag=0
            break
        if a%r==0:
            flag=1
            t//=10
        else:
            flag=0
            break
    if flag==1:
        return 1
    else:
        return 0
a=int(input())
b=int(input())
for i in range(a,b+1):
    if selfdiv(i)==1:
        print(i,end=" ")