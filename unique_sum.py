t=int(input())
a=list(map(int,input().split()))
y=[]
for i in a:
    if i not in y:
        y.append(i)
b=sum(y)
print(b)