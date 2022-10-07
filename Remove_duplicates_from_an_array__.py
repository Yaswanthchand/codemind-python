n=int(input())
a=list(map(int,input().split()[:n]))
k=set(a)
print(*k)