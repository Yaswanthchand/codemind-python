def lcm(m,n):
    l=max(m,n)
    while True:
        if l%m==0 and l%n==0:
            break
        else:
            l+=max(m,n)
    return l
n=int(input())
a=list(map(int,input().split()))
l=lcm(a[0],a[1])
for i in range(2,n):
    l=lcm(l,a[i])
print(l)
