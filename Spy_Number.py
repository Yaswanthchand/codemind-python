n=int(input())
m=1
s=0
while n:
    r=n%10
    m=m*r
    s=s+r
    n=n//10
if(m==s):
    print('Spy Number')
else:
    print("Not Spy Number")