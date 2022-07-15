t=int(input())
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if(a<t or b<t):
        print("UPLOAD ANOTHER")
    elif(a==b):
        print("ACCEPTED")
    else:
        print("CROP IT")