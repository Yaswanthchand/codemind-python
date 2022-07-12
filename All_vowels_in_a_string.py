a=input()
b='aeiou'
c=0
for i in b:
    if i in a:
        c+=1
if c>=5:
    print(True)
else:
    print(False)
        