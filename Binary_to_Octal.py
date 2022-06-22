n=int(input())
for i in range (n):
    a=int(input())
    d=0
    b=1
    while a:
        r=a%10
        a=a//10
        d+=r*b
        b*=2
    x=(oct(d)[2:])
    print(x)