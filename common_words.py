s1=input()
s2=input()
m=s1.lower()
n=s2.lower()
m1=m.split()
n1=n.split()
y=[]
for i in n1:
    if i in m1:
        y.append(i)
print(*y)

