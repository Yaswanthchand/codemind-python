n=input()
a=list(n.split(" "))
x=0
y=0
c=d=0
for i in a:
    x=ord(max(i))
    y=ord(min(i))
    c+=x
    d+=y
print(abs(c-d))