def prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
a=int(input())
b=[]
su=0
for i in range(1,a+1):
    if prime(i)==1 :
        b.append(i)
for j in range(len(b)):
    for k in range(len(b)):
        if(j==k):
            continue
        else:
            if(b[j]*b[k]==a):
                su+=1
                print(b[j],end=' ')
                break
if(su!=2):
    print("-1")