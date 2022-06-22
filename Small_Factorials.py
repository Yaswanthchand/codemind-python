x=int(input())
for i in range (x):
    n=int(input())
    if n==0:
        print(1)
    else:
        fact=1
        for j in range(1,n+1):
            fact=fact*j
        print(fact)