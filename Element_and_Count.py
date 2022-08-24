n=int(input())
a=list(map(int,input().split()))
s=[]
for i in a:
    if i not in s:
        s.append(i)
        print(i,a.count(i),end=' ')