m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
z=[]
for i in a:
    if i in b:
        z.append(i)
k=[]
for i in z:
    if i not in k:
        k.append(i)
print(*k)