n=int(input())
a=list(map(int,input().split()))
k=sorted(a)
k=k[::-1]
if k==a:
    print('yes')
else:
    print('no')