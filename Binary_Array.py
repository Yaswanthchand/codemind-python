n=int(input())
a=list(map(int,input().split()))
for i in a:
    if i==1 or i==0:
        continue
    else:
        print('False')
        break
else:
    print(True)