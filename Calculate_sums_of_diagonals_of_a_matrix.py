n=int(input())
pd=sd=0
for i in range(n):
    a=list(map(int,input().split()))
    for j in range(n):
        if i==j:
            pd+=a[j]
        if i+j==n-1:
            sd+=a[j]
print("Principal Diagonal:",end="")
print(pd)
print("Secondary Diagonal:",end="")
print(sd)
 