n=int(input())
x=0
x1=1
x2=x+x1
c=0
for i in range(100):
    if x1==n:
        c=1
        break
    else:
        x2=x+x1
        x=x1
        x1=x2
        continue
if c==1:
    print("True")
else:
    print("False")