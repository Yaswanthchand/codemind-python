n=input()
n=n.lower()
b=[]
c=0
for i in n:
    if i not in b and i!=' ':
        b.append(i)
print(len(b))