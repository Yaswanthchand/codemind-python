a=input()
b=input()
arr=[]
brr=[]
for i in a:
    if i.isspace():
        continue
    else:
        arr.append(i.lower())
for i in b:
    if i.isspace():
        continue
    else:
        brr.append(i.lower())
rrr=[]
for i in arr:
    if i in brr:
        if i not in rrr:
            rrr.append(i)
rrr.sort()
if len(rrr)==0:
    print(-1)
else:
    for i in rrr:
        print(i,end="")