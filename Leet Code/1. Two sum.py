nums=[2,1,5,3]
target=4

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if(nums[i]+nums[j] == target):
            print(i,j)





