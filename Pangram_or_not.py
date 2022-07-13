a=input()
a=a.lower()
b='qazwsxedcrfvtgbyhnujmikolp'
c=[]
for i in b:
    if i in a:
        c.append(i)
if len(c)>25:
    print(True)
else:
    print(False)
        