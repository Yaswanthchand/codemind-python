n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i not in b:
        b.append(i)
s=0
for i in b:
    if i%2==0:
        s+=i
print(s)