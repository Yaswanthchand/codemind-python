t=int(input())
for j in range (t):
    n=input()
    a=set('0123456789')
    c=0
    c1=0
    for i in range(len(n)):
        c+=1
        if n[i] in a:
            c1+=1
    if(c==c1):
         print(True)
    else:
         print(False)
