a=input()
y=[]
b='aeiouAEIOU'
for i in a:
    if i in b:
        y.append(i)
c=[]
for i in y:
    if i not in c:
        c.append(i)
if len(c)>0:
    print(*c,end=' ')
else:
    print('-1')