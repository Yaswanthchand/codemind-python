n=int(input())
a=list(map(int,input().split()))
sum=0
for i in a:
    while(i>0):
        r=i%10
        i=i//10
        sum=sum+r
print(sum)