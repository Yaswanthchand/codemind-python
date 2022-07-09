n=int(input())
a=list(map(int,input().split()))
x=(len(a)//2)
k=[]
y=[]

for i in range(0,x):
    k.append(a[i])
for i in range(x,n):
    y.append(a[i])
m=sum(k)
b=sum(y)
print(b-m)


    