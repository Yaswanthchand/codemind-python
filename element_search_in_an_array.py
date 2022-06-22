x=int(input())
for i in range (x):
    a=map(int,input().split())
    se=int(input())
    if se in a:
        print(True)
    else:
        print(False)