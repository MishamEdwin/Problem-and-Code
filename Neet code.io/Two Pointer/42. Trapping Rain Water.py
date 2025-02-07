height=[0,2,0,3,1,0,1,3,2,1]


maxval=0
maxLeft=[]
for i in range(len(height)):
    ptr=i

    for j in range(ptr):
        if height[j]>maxval:
            maxval=height[j]
    maxLeft.append(maxval)
print(maxLeft)


maxval=0
maxRight=[]
for i in range(len(height)-1,-1,-1):
    ptr=i

    for j in range(len(height)-1,ptr,-1):
        if height[j]>maxval:
            maxval=height[j]
    maxRight.insert(0,maxval)#insert(position,element)
print(maxRight)


minVal=[]
for i in range(len(height)):
    minVal.append(min(maxLeft[i],maxRight[i]))
print(minVal)


result=[]
for i in range(len(height)):
    sub=minVal[i]-height[i]

    if sub<0:
        result.append(0)
    else:
        result.append(sub)
print(result)

print(sum(result))