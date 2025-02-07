arr=[9,9,9,2,5]

counts={}

#Creating Keys and Values
for elem in arr:
    if elem not in counts:
        counts[elem]=1
    else:
        counts[elem]+=1

print(counts)

#Creating a list[] of (number, count) pairs
count_list=[]

for num in counts:
    count_list.append((num,counts[num]))

print(count_list)

#Sort by count first then number

def custom_sort(pair):
    return(-pair[1],pair[0])

count_list.sort(key=custom_sort)

#using lambda function
#count_list.sort(key=lambda x: (-x[1], x[0]))

print(count_list)

#print elements based on frequency

for num,count in count_list:
    print((str(num) + ' ')*count,end="")


















"""
#traversal of dictionary
for i in counts:
    print(i,counts[i])
"""


