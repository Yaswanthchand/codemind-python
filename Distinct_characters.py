n=input()
n=n.lower()
b=[]
for i in n:
    if i not in b and i!=' ':
        b.append(i)
b=sorted(b)
for j in b:
    print(j,end='')