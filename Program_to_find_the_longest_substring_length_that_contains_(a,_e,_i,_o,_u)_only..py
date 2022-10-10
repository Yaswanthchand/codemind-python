n=input()
n=n.lower()
c=0
b=[]
for i in n:
    if(i=='a' or i=='e' or i=='i' or i=="o" or i=='u'):
        c+=1
    else:
        b.append(c)
        c=0
b.append(c)
print(max(b))