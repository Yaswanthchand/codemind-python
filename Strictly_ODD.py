n=int(input())
a=list(map(int,input().split()))
y=[]
for i in range(len(a)):
    if a[i]%2==1:
        y.append(i)
c=0
for j in y:
    if j%2==1:
        c+=1
if(c==len(y)):
    print(True)
else:
    print(False)