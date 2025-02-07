n=5
arr=input().split()
result=[]
sort=[]

for i in range(n):
    arr[i]=int(arr[i])

for i in range(n+1):
    result.append(0)
    sort.append(0)

print(arr)
print(result)

for i in arr:
    if result[i]>n:
        print(result)
    else:
        result[i] += 1

for elem in result:
    print(elem,end=' ')
sortidx=0
for i in range(len(result)):
    while(result[i]>0):
        sort[sortidx]=i
        sortidx+=1
        result[i]-=1

print(sort)