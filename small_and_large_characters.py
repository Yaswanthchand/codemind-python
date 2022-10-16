n=input()
a=list(n.split(" "))
x=0
y=0
c=[]
for i in a:
    x=(max(i))
    y=(min(i))
    c.append(y)
    c.append(x)
print(*c)