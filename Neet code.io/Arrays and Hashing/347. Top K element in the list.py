nums = [1,2,2,3,3,3]
k = 2

dictionary={}
result=[]
for elem in nums:
    if elem not in dictionary:
        dictionary[elem]=1
    else:
        dictionary[elem]+=1

print(dictionary)

count_list=[]

for elem in dictionary:
    count_list.append((elem,dictionary[elem]))

print(count_list)

count_list.sort(key=lambda x: (-x[1],x[0]))
print(count_list)

for item in count_list:
    result.append(item[0])

print(result[:k])