n=int(input())
a=list(map(int,input().split()))
for i in a:
    sum=0
    while(i>0):
        r=i%10
        i=i//10
        sum=sum*10+r
    print(sum,end=' ')