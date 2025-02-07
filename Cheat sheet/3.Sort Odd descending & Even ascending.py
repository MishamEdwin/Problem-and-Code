arr=[1, 2, 3, 5, 4, 7, 10]

odd=[]

even=[]

merged=[]

for elem in arr:

    if elem%2 == 0:
        even.append(elem)

    elif elem ==0:
        even.append(elem)

    else:
        odd.append(elem)


#ascend
for i in range(len(odd)):
    for j in range(len(odd)-i-1):
        if(odd[j]<odd[j+1]):
            temp=odd[j]
            odd[j]=odd[j+1]
            odd[j+1]=temp

#descend

for i in range(len(even)):
    for j in range(len(even)-i-1):
        if (even[j]>even[j+1]):
            temp=even[j]
            even[j]=even[j+1]
            even[j+1]=temp


for elem in odd:
    merged.append(elem)

for elem in even:
    merged.append(elem)

print(merged)