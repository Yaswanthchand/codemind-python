n=int(input())
a=list(map(int,input().split()))
k=sorted(a)
b=k[::-1]
if b==a:
    print("yes")
else:
    print('no')