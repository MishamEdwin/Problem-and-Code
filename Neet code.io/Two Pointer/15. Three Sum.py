nums = [0,1,1]

res=[]
nums.sort()
print(nums)

for i,a in enumerate(nums):
    if i>0 and a==nums[i-1]:
        continue

    l=i+1
    r=len(nums)-1

    while l<r:
        threesum=a+nums[l]+nums[r]

        if threesum > 0:
            r-=1
        elif threesum < 0:
            l+=1
        else:
            res.append([a,nums[l],nums[r]])
            l+=1

print(res)

""" Brute Force - 3 loops 
nums=sorted(nums)

output=[]
res=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            arr=[]
            if nums[i]+nums[j]+nums[k] ==0:
                arr.append(nums[i])
                arr.append(nums[j])
                arr.append(nums[k])
                output.append(arr)

print(output)

for elem in output:
    if elem not in res:
        res.append(elem)

print(res)"""