a=input()
b=input()
a1=""
b1=""
for i in a:
    if i.isupper():
        a1+=i.lower()
    else:
        a1+=i
for i in b:
    if i.isupper():
        b1+=i.lower()
    else:
        b1+=i
arr=list(a1.split())
brr=list(b1.split())
res=[]
for i in brr:
    if i in arr:
        if i not in res:
            res.append(i)
if len(res)==0:
    print(0)
else:
    for i in res:
        print(i,end=" ")