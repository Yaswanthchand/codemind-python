n=int(input())
for i in range(0,n//2+1):
    if n==i*i:
        print(True)
        break
else:
    print(False)