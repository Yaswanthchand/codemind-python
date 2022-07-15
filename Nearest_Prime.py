n=int(input())
for i in range(n):
    x=0
    y=0
    c=0
    d=0
    a=int(input())
    for j in range(a,1,-1):
        for k in range(2,int(j**0.5)+1):
            if(j%k==0):
                break
        else:
            x=j
            break
    for m in range(a,a+1000,1):
        for l in range(2,int(m**0.5)+1):
            if(m%l==0):
                break
        else:
            y=m
            break
    c=a-x
    d=y-a
    if(c<=d):
        print(x)
    else:
        print(y)
    