n=int(input())
a=list(map(int,input().split()))
sume=0
sumo=0
for i in range(n):
    if(i%2==0):
        sume=sume+a[i]
    else:
        sumo=sumo+a[i]
if(sume-sumo==0):
    print('YES')
else:
    print('NO')