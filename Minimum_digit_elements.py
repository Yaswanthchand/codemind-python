n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    c=0
    if a==0:
        b.append(i)
        continue
    while(i):
        c+=1
        i//=10
    b.append(c)
k=min(b)
print(b.count(k))