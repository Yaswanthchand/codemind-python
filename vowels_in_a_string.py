n=input()
x=input()
for i in n:
    if(i==x):
        print(True)
        print(n.index(i))
        break
else:
    print(False)