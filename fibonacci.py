n=int(input())
x=0
x1=1
x2=0
for i in range(n):
    print(x,end=" ")
    x2=x+x1
    x=x1
    x1=x2