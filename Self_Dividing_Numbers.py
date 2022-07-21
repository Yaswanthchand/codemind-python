def num(n):
    t=n
    d=0
    f=0
    while(n):
        r=n%10
        d+=1
        if(r!=0):
            if t%r==0:
                f+=1
        n=n//10
    if d==f:
        return True
    else:
        False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if num(i):
        print(i,end=' ')
    
                