height = [1,8,6,2,5,4,8,3,7]
area_list=[]
left=0
right=len(height)-1
print(right)

while left<right:
    breadth=right-left
    length=min(height[left],height[right])

    area=length*breadth
    area_list.append(area)

    if(height[left]<height[right]):
        left+=1
    else:
        right-=1

print(area_list)
print(max(area_list))