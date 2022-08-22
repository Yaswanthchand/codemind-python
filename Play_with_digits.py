n=int(input())
a=list(map(int,input().split()))
r=0
s=0
for i in a:
    k=i
    while k:
        d=k%10
        s+=d
        k//=10
print(s)