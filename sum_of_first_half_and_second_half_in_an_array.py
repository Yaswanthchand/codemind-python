n=int(input())
a=list(map(int,input().split()))
s=0
s1=0
for i in range(n//2):
    s=s+a[i]
for i in range(n//2,n):
    s1=s1+a[i]
print(s)
print(s1)