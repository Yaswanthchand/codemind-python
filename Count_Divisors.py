i,r,k=map(int,input().split())
c=0
for n in range(i,r+1):
    if n%k==0:
        c+=1
print(c)