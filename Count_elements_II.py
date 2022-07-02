m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=set(a)
y=set(b)
z=[]
for i in x:
    if i not in y:
        z.append(i)
for i in y:
    if i not in x:
        z.append(i)
print(len(z))