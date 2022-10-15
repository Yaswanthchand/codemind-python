n=input()
n=n.lower()
c=d=0
for i in n:
    if i!=' ':
        c+=1
    if i.isalpha():
        d+=1
print(c-d)