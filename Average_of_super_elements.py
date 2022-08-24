n=int(input())
a=list(map(int,input().split()))
s=0
c=0
k=0
b=[]
for i in a:
    if a.count(i)==i and i not in b:
        c+=1
        b.append(i)
        k=1
        s=s+i
if k==0:
    print(-1)
else:
    print('{:.2f}'.format(s/c))