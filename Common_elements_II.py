m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
y=[]
for i in a:
    if i not in b:
        y.append(i)
for i in b:
    if i not in a:
        y.append(i)
print(*y)