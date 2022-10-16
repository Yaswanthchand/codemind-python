n=input()
n=n.lower()
for i in n:
    if(n.count(i)==1 and(i!=' ')):
        print(i)
        break
else:
    print("-1")