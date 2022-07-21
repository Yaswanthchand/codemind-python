a=int(input())
for i in range(a,2,-1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        break
for m in range(a+1,a+100):
    for n in range(2,m):
        if m%n==0:
            break
    else:
         break
if abs(a-m)>=abs(a-i):
    print(abs(a-i))
else:
    print(abs(a-m))