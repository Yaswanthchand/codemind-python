n=int(input())
for i in range(n):
    if(pow(2,i)>n):
        x=abs(n-pow(2,i))
        y=abs(n-pow(2,i-1))
        if(x>y):
            print(y)
            break
        else:
            print(x)
            break