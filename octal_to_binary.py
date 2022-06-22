n=int(input())
d=0
b=1
while n:
    r=n%10
    d=d+r*b
    b=b*8
    n=n//10
print(bin(d)[2:])