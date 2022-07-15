n=int(input())
a=list(map(int,input().split()))
x=a[0]
j=1
while j<n:
    if a[j]%x==0:
        j+=1
    else:
        x=a[j]%x
print(x)