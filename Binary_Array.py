t=int(input())
a=list(map(int,input().split()))
for i in range(t):
    if a[i]!=0 and a[i]!=1:
        print(False)
        break
else:
    print(True)