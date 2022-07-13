a=input()
a=a.lower()
a=list(a)
b=[]
for i in a:
    if i not in b:
        b.append(i)
if(b==a):
    print('True')
else:
    print('False')
