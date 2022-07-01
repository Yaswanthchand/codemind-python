def rev(a):
    s=0
    while a>0:
        r=a%10
        s=(s*10)+r
        a//=10
    return s
n=int(input())
rev1=rev(n)
sum=0
j=1
while rev1>0:
    r=rev1%10
    sum+=r**j
    j+=1
    rev1//=10
if sum==n:
    print(True)
else:
    print(False)