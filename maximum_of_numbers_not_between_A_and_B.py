x=int(input())
a=list(map(int,input().split()))
m,n=map(int,input().split())
c=[]
for i in a:
    if i<m or i>n:
        c.append(i) 
if len(c)>0:
    print(max(c))
else:
    print('-1')
