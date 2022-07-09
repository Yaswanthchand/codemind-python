n=int(input())
a=list(map(int,input().split()))
k=set(a)
b=sorted(k)
if b==a:
    print('yes')
else:
    print('no')