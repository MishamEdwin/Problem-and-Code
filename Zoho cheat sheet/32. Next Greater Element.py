arr=[1, 3, 2, 4]
res=[]

for i in range(len(arr)):
    ans=-1
    for j in range(i+1,len(arr)):
        if arr[j]>arr[i]:
            ans=arr[j]
            break # this prevents excessive iteration
    res.append(ans)

print(res)