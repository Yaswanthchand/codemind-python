n=int(input())
n1=n*n
s=0
while(n1):
    r=n1%10
    s+=r
    n1//=10
if s==n:
    print('Neon Number')
else:
    print('Not Neon Number')
    