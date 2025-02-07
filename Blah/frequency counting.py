arr=[5,5,4,6,4]

nums=[]
count=[]

for elem in arr:
    if elem in nums:
        index=nums.index(elem)
        count[index]+=1
    else:
        nums.append(elem)
        count.append(1)

print(nums)
print(count)


