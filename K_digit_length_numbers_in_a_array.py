n,k=map(int,input().split())
a=list(map(int,input().split()))
x=0
for i in range(n):
    if a[i]<0:
        a[i]=a[i]*(-1)
    c=0
    if a[i]==0:
        c=1
    y=a[i]
    while y:
        d=y%10
        y//=10
        c+=1
    if k==c:
        x+=1
print(x)
        