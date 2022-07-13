a=int(input())
b=0
c=0
d=0
r=0
rev=0
while a>0:
    r=a%10
    b=b*10+r
    a//=10
while b>0:
    c=b%10
    b//=10
    if d<1:
        if c==6:
            c=9
            d=1
    rev=rev*10+c
print(rev)