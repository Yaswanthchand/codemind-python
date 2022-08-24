n=int(input())
a=list(map(int,input().split()))
m=int(input())
m=a.index(m)
s=0
for i in range(m+1):
    s+=a[i]
print(s)