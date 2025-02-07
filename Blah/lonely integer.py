n=int(input())
a=input().split()

for i in range(len(a)):
    a[i]=int(a[i])



lonely=0

for elem in a:
    lonely^=elem
print(lonely)


