a=int(input())
c=0
for i in range(2,int(a**0.5)):
    if a%i==0:
        print("Not Mega Prime")
        break
else:
    while a:
     d=a%10
    # print(d)
     if d==1 or d==0:
         c=1
         break
     for j in range(2,d):
        if d%j==0:
            c=1
            break
     a=a//10
    if c!=1:
        print("Mega Prime")
    else:
        print("Not Mega Prime")