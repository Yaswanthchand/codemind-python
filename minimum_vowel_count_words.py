n=input()
v='aeiouAEIOU'
b=[]
x=z=y=0
for i in n:
    if(i==" "):
        b.append(x)
        x=0
    if(i in v):
        x+=1
b.append(x)
y=min(b)
for i in b:
    if(i==y):
        z+=1
print(z)