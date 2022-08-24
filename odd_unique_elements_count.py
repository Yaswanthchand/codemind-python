n=int(input())
a=list(map(int,input().split()))
s=set(a)
c=0
for i in s:
    if i%2!=0:
        c+=1
print(c)