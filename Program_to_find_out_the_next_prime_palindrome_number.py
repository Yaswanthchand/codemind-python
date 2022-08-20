def prime(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1
def palindrome(k):
    t=k
    r=0
    while(t):
        d=t%10
        r=r*10+d
        t=t//10
    if r==k:
        return 1
    else:
        return 0
n=int(input())
for i in range(n+1,10000000):
    if prime(i):
        if palindrome(i):
            print(i)
            break
        
        
        