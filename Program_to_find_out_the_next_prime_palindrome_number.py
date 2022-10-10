def prime(n):
    for i in range(2,int((n**0.5)+1)):
        if(n%i==0):
            return 0
    else:
        return 1
def palindrome(n):
    temp=n
    s=0
    while(n>0):
        l=n%10
        s=s*10+l
        n=n//10
    if(s==temp):
        return 1
    else:
        return 0
n=int(input())
for i in range(n+1,100000):
    if(prime(i) and palindrome(i)):
        print(i)
        break