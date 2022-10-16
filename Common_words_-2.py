n=input()
m=input()
a=list(n.split(" "))
b=list(m.split(" "))
c=0
for i in a:
    if i in b:
        if(a.count(i)==1):
            if(b.count(i)==1):
                c+=1
print(c)