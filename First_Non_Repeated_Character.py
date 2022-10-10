t=int(input())
for k in range(t):
    a=int(input())
    b=input()
    for i in b:
        x=b.count(i)
        if(x==1):
            print(i)
            break
    else:
        print("-1")
        