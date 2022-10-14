n,k=map(int,input().split())
a=list(map(int,input().split()))
y=0
for i in a:
    c=0
    if(i<0):
        i=i*(-1)
    if(i==0):
        c+=1
    while(i>0):
        j=i%10
        i=i//10
        c+=1
    if(c==k):
        y+=1
print(y)