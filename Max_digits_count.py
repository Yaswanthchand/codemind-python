def fun(n):
    c=0
    while(n):
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
print(b.count(m))