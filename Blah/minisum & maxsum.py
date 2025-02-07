n=5
arr=input().split()

for i in range(len(arr)):
    arr[i]=int(arr[i])

sums=[]

for i in range(len(arr)):
    total=sum(arr)-arr[i]
    sums.append(total)
print(arr)
print(sums)
print(sums[-1],sums[0])
