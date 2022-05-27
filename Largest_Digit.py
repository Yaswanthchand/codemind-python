n=int(input())
max=0
while n:
    r=n%10
    if r>max:
        max=r
    n=n//10
print(max)
    