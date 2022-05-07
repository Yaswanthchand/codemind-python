n=int(input())
n1=n*n
r1=0
while n:
    r=n%10
    r1=r1*10+r
    n=n//10
n2=r1*r1
r2=0
while n2:
    r=n2%10
    r2=r2*10+r
    n2=n2//10
if(r2==n1):
    print('True')
else:
    print('False')
    


