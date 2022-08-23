n=int(input())
a=list(map(int,input().split()))
s=sum(a)//n
for i in a:
    if i==s:
        print(True)
        break
else:
    print(False)