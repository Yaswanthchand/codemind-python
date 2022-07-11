a=input()
b=input()
c=0
for i in a:
    if i==b:
        c+=1
    elif b not in a:
        c=-1
print(c)
    
