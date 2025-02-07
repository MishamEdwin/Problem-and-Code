"""
input:
   target=7
   nums=[2,3,1,2,4,3]

output:
   2

explanation:
   The subarray[4:3] has the minimal length under the problem constraint

"""

nums=[2,3,1,2,4,3]
target=7

front=0
back=1

minsum=[]

for i in range(len(nums)):
    subarray=[]
    for j in range(front,back):
        subarray.append(nums[j])
    back+=1
    minsum.append(subarray)

print(minsum)

for i in minsum:
    print(i,sum(i))




