n=int(input())
a=list(map(int,input().split()))
x=0
for i in range(n-1,0,-1):
    if(a[i]%2==0):
        x=i
        break
if(x==0):
    print('0')
else:
    print(x)