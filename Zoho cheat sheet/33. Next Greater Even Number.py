from itertools import permutations
x = 34722641
x=list(str(x))
arr=[]

for elem in x:
    elem=int(elem)
    arr.append(elem)
print(arr)


mineve=[]

for i in range(len(arr)):
    if arr[i]%2==0:
        mineve.append(arr[i])
#print(mineve)
minn=min(mineve)
print(minn)


res=[]
front=""
for i in range(len(arr)):
    if arr[i]==minn:
        res=arr[i-1:]
        front=arr[:i-1]
print(res)


perms=[]

for p in permutations(res):
    temp=""
    for digits in p:
        temp+=str(digits)
    temp=int(temp)
    if temp%2==0:
        perms.append(temp)

perms=set(perms)
perms=sorted(perms)
print(perms)

res=tuple(res)
print(res)

new_res=""
for elem in res:
    new_res+=str(elem)

new_res=int(new_res)
print(new_res)

back=0

for nums in perms:
    if int(nums)> new_res:
        back=int(nums)
        break

print(back)

print(front)
new_front=""
for elem in front:
    new_front+=str(elem)

print(new_front)

ans=new_front+str(back)
print(ans)


