a=input()
c=0
b='aeiouAEIOU'
for i in a:
    if i in b:
        c+=1
print(c)