N=4
nums=[]
for i in range((-N*2)+1,N*2):
    if i == 0:
        continue
    elif i == 1 and (i in nums):
        continue
    else:
        nums.append(abs(i))
print(nums)

space=N-1
mid=len(nums)//2

#left pointers
l2=mid-1
l1=mid-2

#right pointers
r1=mid
r2=mid+1


for i in range(N):
    print(" "*space,end="")
    space-=1

    #first line
    if i == 0 :
        print(nums[mid])
    else:
        #left
        for j in range(l2,l1-1,-1):
            print(nums[j],end="")

        #right
        for k in range(r2,r1,-1):
            print(nums[k],end="")

        print()
        l2 -= 1
        l1 -= 2
        r1 += 1
        r2 += 2






