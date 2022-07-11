m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
y=[]
for i in b:
    if i in a and i not in y:
        y.append(i)
if y==b:
    print('Yes')
else:
    print('No')