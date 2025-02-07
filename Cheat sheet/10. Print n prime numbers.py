n=10

def isprime(n):
    if n==0 or n==1:
        return False

    for i in range(2,n):
        if(n%i==0):
            return False

    return True

for i in range(2,n+1):
    if(isprime(i)):
        print(i,end=" ")