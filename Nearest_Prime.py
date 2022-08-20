def prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
def near(a):
    x=0
    y=0
    dx=0
    dy=0
    for i in range(a,0,-1):
        if prime(i)==1:
            y=i
            dy=a-i
            break
    for i in range(a,10000):
        if prime(i)==1:
            l=i
            dx=i-a
            break
    if dy==dx:
        return y
    elif dy>dx:
        return l
    elif dy<dx:
        return y
t=int(input())
for i in range(t):
    a=int(input())
    print(near(a))