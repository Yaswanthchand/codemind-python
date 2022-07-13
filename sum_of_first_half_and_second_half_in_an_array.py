n=int(input())
a=list(map(int,input().split()))
c=0
c1=0
for i in range(0,len(a)//2):
    c+=a[i]
for i in range(len(a)//2,len(a)):
    c1+=a[i]
print(c)
print(c1)