n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n-2):
    x=a[i]
    z=a[i+2]
    if (x%2==0 and z%2==1) or (x%2==1 and z%2==0):
        c+=1
print(c)