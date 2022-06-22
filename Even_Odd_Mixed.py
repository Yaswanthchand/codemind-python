n=int(input())
e=0
od=0
while n:
    r=n%10
    if(r%2==0):
        e+=1
    else:
        od+=1
    n=n//10
if e>0 and od==0:
    print("Even")
if e==0 and od>0:
    print("Odd")
if e>0 and od>0:
    print("Mixed")
        