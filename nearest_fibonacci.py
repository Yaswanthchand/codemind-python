n=int(input())
a=[]
fa=0
fb=1
fn=fa+fb
for i in range(100):
    a.append(fa)
    fn=fa+fb
    fa=fb
    fb=fn
f=l=df=fl=0
for i in range(100):
    if a[i]>n:
        l=a[i]
        f=a[i-1]
        dl=l-n
        df=n-f
        if df==dl:
            print(f,l)
        elif df>dl:
            print(l)
        elif df<dl:
            print(f)
        break