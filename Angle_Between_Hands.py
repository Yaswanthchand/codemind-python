n=input()
h=(ord(n[0])-48)*10+(ord(n[1])-48)
m=(ord(n[3])-48)*10+(ord(n[4])-48)
if m%2==0:
    a=30*h-((11*m*1.0)//2)
    if a<0:
        a+=360
    if a>180:
        a=360-a
    print("{:.1f}".format(a))
else:
    a=(30*h*1.0)-(11*m*1.0/2)
    if a<0:
        a+=360
    if a>180:
        a=360-a
    print("{:.1f}".format(a))