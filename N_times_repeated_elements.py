n=int(input())
a=list(map(int,input().split()))
k=int(input())
y=[]
c=0
for i in range(n):
    if a.count(a[i])==k and a[i] not in y:
        y.append(a[i])
        c=1
if c==0:
    print(-1)
else:
    print(*y)