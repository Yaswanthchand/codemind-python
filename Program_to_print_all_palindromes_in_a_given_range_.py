a=int(input())
b=int(input())
for i in range(a,b+1,1):
    temp=i
    rev=0
    while(i):
        r=i%10
        rev=rev*10+r
        i=i//10
    if(rev==temp):
        print(rev,end=' ')