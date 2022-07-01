n=input()
n1='abcdefghijklmnopqrstuvwxyz'
x=[]
y=[]
for i in n:
    if i in n1:
        x.append(i)
    else:
        y.append(i)
c=0
for j in y:
    c+=int(j)
print(c)
    
