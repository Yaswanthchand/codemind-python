n=int(input())
for i in range (n):
    a=int(input())
    d=0
    b=1
    while a:
        r=a%10
        d=d+r*b
        b=b*2
        a=a//10
    print(d)