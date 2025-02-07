n=int(input())
s=input().split()

for i in range(n):
    s[i]=int(s[i])

d,m=map(int,input().split())

print(s)
print(d)
print(m)

result=[]

for i in range(len(s)-m+1):
    subarray=s[i:i+m]
    if sum(subarray)==d:
        result.append(subarray)

for i in result:
    print(i,end=" ")





"""s=[2,2,1,3,2]
d=4
m=2

result=[]

for i in range(len(s)-m+1):
    subarray=s[i:i+m]
    if sum(subarray)==d:
        result.append(subarray)

for i in result:
    print(i,end=' ')
    
print(len(result))







"""