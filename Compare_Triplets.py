a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
d=0
for i in range(0,len(a)):
    if(a[i]>b[i]):
        c+=1
    elif(a[i]==b[i]):
        c+=0 
    else:
        d+=1
print(c,d,end='')