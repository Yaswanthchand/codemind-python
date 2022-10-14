n=input()
c=0
b=[]
for i in n:
    if(i==' '):
        b.append(c)
        c=0
    else:
        c+=1
b.append(c)
print(*b)