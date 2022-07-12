a=input()
b='QAZWSXEDCRFVTGBYHNUJMIKOLP'
c=[]
for i in a:
    if i in b:
        c.append(i)
print(len(c))