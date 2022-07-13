n=int(input())
a=list(map(int,input().split()))
k=set(a)
c=0
for i in k:
    if i%2==1:
        c+=1
print(c)