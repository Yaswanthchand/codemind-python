n=int(input())
a=list(map(int,input().split()))
s=0
for i in range (n):
    if i%2==0:
        r=a[i]
        s=s+r
print(s)