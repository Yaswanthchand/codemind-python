t=int(input())
a=list(map(int,input().split()))
m=[]
n=[]
for i in range(0,len(a)):
    if i%2==1:
        m.append(a[i])
    elif i%2==0:
        n.append(a[i])
y=sum(m)
z=sum(n)
print(z-y)