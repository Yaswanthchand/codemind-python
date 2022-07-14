def fun(n):
    c=0
    while(n):
        if n<0:
            n=n*(-1)
        r=n%10
        c+=1
        n//=10
    return c
x=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    b.append(fun(i))
m=max(b)
for i in range(x):
    if b[i]==m:
        print(a[i],end=' ')
        
        
        
        
        
        
        
        
        
        
        