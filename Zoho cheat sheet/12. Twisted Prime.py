N=97

rev=str(N)
rev=rev[::-1]
rev=int(rev)

def isprime(n):

    if n==1 or n==0:
        return False

    for i in range (2,n):
        if (n%i==0):
            return False

    return True

if isprime(N) and isprime(rev):
    print(1)
else:
    print(0)
