n=int(input())
temp=n
m=1
s=0
while(n):
    r=n%10
    m=m*r
    s=s+r
    n=n//10
res=m-s
print(res)