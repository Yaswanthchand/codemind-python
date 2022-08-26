t=int(input())
a=list(map(int,input().split()))
m,n=map(int,input().split())
k=0
min=0
for i in range(t):
    if a[i]>=m and a[i]<=n:
        k=1
        min=min+a[i]
if k==0:
    print(-1)
else:
    print(min)
        