def happy(a):
    s=0
    while(1):
        s=0
        while a>0:
            r=a%10
            s+=r**2
            a//=10
        if s<10:
            break
        else:
            a=s
            continue
    if s==1 or s==7:
        return 1
    else:
        return 0
n=int(input())
res=happy(n)
if res==1:
    print(True)
else:
    print(False)