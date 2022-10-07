n=int(input())
a=list(map(int,input().split()))
num=0
for i in a:
    num=(num*10)+i
num+=1
a2=[]
while num>0:
    r=num%10
    a2.append(r)
    num//=10
a2.reverse()
for i in a2:
    print(i,end=" ")