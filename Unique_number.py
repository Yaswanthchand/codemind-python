n=int(input())
x=str(n)
y=list(x)
b=[]
for i in y:
    if i not in b:
        b.append(i)
if(b==y):
    print('Unique Number')
else:
    print('Not Unique Number')
    