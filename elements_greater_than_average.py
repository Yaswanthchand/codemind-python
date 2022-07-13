n=int(input())
a=list(map(int,input().split()))
b=sum(a)
c=b//n
s=0
for i in a:
    if i>=c:
        s+=1
print(s)