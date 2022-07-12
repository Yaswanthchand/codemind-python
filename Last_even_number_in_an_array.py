n=int(input())
a=list(map(int,input().split()))
max=0
for i in (a):
    if i%2==0:
        r=i
        if(r>max):
            max=r
print(max)