n=input()
v='aeiouAEIOU'
c=0
b=[]
for i in n:
    if(i==' '):
        b.append(c)
        c=0
    if i in v:
        c+=1
b.append(c)
print(*b)