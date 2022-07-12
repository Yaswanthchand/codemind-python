x=int(input())
a=list(map(int,input().split()))
m,n=map(int,input().split())
sum=0
for i in a:
    if i<m or i>n:
        sum+=i
print(sum)