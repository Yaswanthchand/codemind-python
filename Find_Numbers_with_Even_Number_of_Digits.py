n=int(input())
a=list(map(int,input().split()))
d=0
for i in a:
    c=0
    while (i):
        j=i%10
        i=i//10
        c+=1
    if(c%2==0):
        d+=1
print(d)