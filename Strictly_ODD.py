n=int(input())
a=list(map(int,input().split()))
c=d=0
for i in range(n):
    if(i%2==1):
        if(a[i]%2==1):
            c+=1
for i in a:
    if(i%2==1):
        d+=1
if(c==d):
    print(True)
else:
    print(False)
    