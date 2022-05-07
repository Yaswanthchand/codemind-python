n=int(input())
rev=0
temp=n
if n<0:
    n=n*(-1)
while n:
    r=n%10
    rev=rev*10+r
    n=n//10
if temp<0:
    rev=rev*(-1)
    print(rev)
else:
    print(rev)