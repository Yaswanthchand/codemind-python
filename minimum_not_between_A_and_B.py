n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
b=[]
for i in a:
    if(i<x or i>y):
        b.append(i)
if(len(b)>0):
    print(min(b))
else:
    print("-1")