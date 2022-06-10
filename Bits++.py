n=int(input())
res=0
for i in range(n):
    t=input()
    if t=='++X':
        res+=1
    if t=='X++':
        res+=1
    if t=='--X':
        res-=1
    if t=='X--':
        res-=1
print(res)