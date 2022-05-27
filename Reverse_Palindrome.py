def rev_p(n):
    r=0
    while n>0:
        rem=n%10
        r=(r*10)+rem
        n//=10
    return r
n=int(input())
n=n+rev_p(n)
while n>0:
    if n==rev_p(n):
      break
    else:
      n=n+rev_p(n)
print(n)
    

    