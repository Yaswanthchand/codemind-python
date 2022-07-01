import math
def fun(a):
    c=0
    while a>0:
        r=a%10
        c+=1
        a//=10
    return c
a=int(input())
n=fun(a)
y=a*a
if y%math.pow(10,n)==a:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")