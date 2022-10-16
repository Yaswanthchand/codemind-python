n=input()
n=n.lower()
x=''
c=0
for i in n.split(" "):
    x=i
    d=0
    for j in x:
        if j in "aeiou":
           d=1
           break
        else:
            break
    x=x[::-1]
    for k in x:
        if k not in "aeiou":
            d+=1
            break
        else:
            break
    if (d==2):
        c+=1
print(c)