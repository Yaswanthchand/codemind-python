n=int(input())
a=list(map(int,input().split()))
k=n//2
for i in range(n-1,k-1,-1):
    print(a[i],end=" ")
for i in range(k):
    print(a[i],end=" ")