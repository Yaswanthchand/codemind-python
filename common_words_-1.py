n=input()
m=input()
n=n.lower()
m=m.lower()
a=list(n.split(" "))
b=list(m.split(" "))
c=0
for i in a:
    if i in b:
        c+=1
print(c)