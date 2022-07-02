n=int(input())
a=list(map(int,input().split()))
for i in range(0,n,2):
    x=a[i]
    y=a[i+1]
    for j in range(y):
        print(x,end=' ')