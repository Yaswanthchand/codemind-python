import math
a,b,c=map(int,input().split())
s=float(a+b+c)/2.0
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print('{:.2f}'.format(area))