t=int(input())
a=list(map(int,input().split()))
s=[str(i) for i in a]
x= "".join(s)
r=int(x)
d=0
b=1
while(r):
    rem=r%10
    d=d+rem*b
    b*=2
    r//=10
print(d)
    
