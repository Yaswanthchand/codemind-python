n=input()
b=[]
x=''
y=''
for i in n.split(" "):
    x=i
    b.append(min(x))
    break
for i in n.split(" "):
    y=i
b.append(max(y))
print(*b)