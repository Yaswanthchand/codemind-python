n=input()
x=n.lower()
s1='bcdfghjklmnpqrstvwxyz'
s2='aeiou'
v=[]
c=[]
d=[]
s=[]
for i in x:
    if i in s2:
        v.append(i)
    elif i in s1:
        c.append(i)
    elif i==' ':
        s.append(i)
    else:
        d.append(i)
print('Vowels:',len(v))
print('Consonants:',len(c))
print('Digits:',len(d))
print('White spaces:',len(s))
        