n=int(input())
a=list(map(int,input().split()))
if n%2!=0:
    a.append(0)
print(*a)