a=input()
b=input()
a=a.lower()
b=b.lower()
c=[]
for i in a:
    if i in b:
        if i==' ':
            continue
        if i not in c:
            c.append(i)
print(len(c))