n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if(i<0):
        i=i*(-1)
    if(i==0):
        i=1
    c=0
    while(i):
        x=i%10
        i=i//10
        c+=1
    b.append(c)
print(*b)