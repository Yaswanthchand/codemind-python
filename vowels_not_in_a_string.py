a=input()
y=[]
b='aeiou'
for i in b:
    if i not in a:
        y.append(i)
if len(y)>0:
    print(*y,end=' ')
else:
    print('0')
