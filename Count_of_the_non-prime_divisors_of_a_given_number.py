def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
n=int(input())
count=0
for i in range(1,n+1):
    if prime(i)!=1 and n%i==0:
        count+=1
print(count)