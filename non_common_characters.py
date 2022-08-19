a=input()
b=input()
a1=""
b1=""
for i in a:
    if i.isspace():
        continue
    else:
        a1+=i.lower()
for i in b:
    if i.isspace():
        continue
    else:
        b1+=i.lower()
arr=[]
for i in a1:
    if i not in b1:
        if i not in arr:
            arr.append(i)
for i in b1:
    if i not in a1:
        if i not in arr:
            arr.append(i)
arr.sort()
if len(arr)==0:
    print(0)
else:
    for i in arr:
        print(i,end="")