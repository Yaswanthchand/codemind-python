n=input()
a=list(n.split(" "))
b=[]
for i in range(len(a)):
    if(i%2==0):
        b.append(a[i][::-1])
    else:
        b.append(a[i])
print(*b)