m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=set(a)
y=set(b)
z=[]
for i in x:
    if i in y:
        z.append(i)
print(len(z))