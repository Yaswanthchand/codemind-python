def add(a):
    sum=0
    t=a
    while True:
        sum=0
        while t>0:
            r=t%10
            sum+=r
            t//=10
        if sum<10:
            return sum
        else:
            t=sum
            sum=0
            continue
a=int(input())
res=add(a)
print(res)
