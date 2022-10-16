n=input()
a=list(n.split(" "))
x=0
y=0
c=[]
for i in a:
    x=ord(max(i))
    y=ord(min(i))
    c.append(x-y)
print(*c)