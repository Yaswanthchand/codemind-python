n=int(input())
arr=list(map(int,input().split()))
c=0
for i in arr:
    if i<n:
        c+=1
    else:
        c=0
        break
if c>=1:
    print('YES')
else:
    print('NO')
        
 