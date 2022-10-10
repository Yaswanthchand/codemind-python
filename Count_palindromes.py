n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    sum=0
    temp=a[i]
    while(a[i]):
        j=a[i]%10
        sum=sum*10+j
        a[i]=a[i]//10
    if(sum==temp):
        c+=1
print(c)