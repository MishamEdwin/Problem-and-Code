nums = [1,2,4,6]
output=[]
#Output: [48,24,12,8]

for i in nums:
    prod=1

    for j in nums:
        if i==j:
            continue
        else:
            prod*=j

    output.append(prod)

print(output)


"""prod=1

for elem in nums:
    prod*=elem
print(prod)

for elem in nums:
    temp=prod//elem
    output.append(temp)

print(output)"""