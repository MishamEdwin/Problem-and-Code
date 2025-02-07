nums = [2,20,4,10,3,4,5]

output=[]
ptr=0

nums=sorted(nums)
print(nums)

nums=list(set(nums))

for i in range(len(nums)):
    if i < len(nums)-1:
        if nums[ptr]+1==nums[i+1]:
            output.append(nums[ptr])
            ptr+=1

if output[-1]+1==nums[ptr]:
    output.append(nums[ptr])


print(output, len(output))










