arr=[3, 4, 2, 3, 16, 3, 15, 16, 15, 15, 16, 2, 3]
count={}

for elem in arr:
    if elem not in count:
        count[elem]=1
    else:
        count[elem]+=1
print(count)

sorted_count=sorted(count.items(),reverse=True,key=lambda x: x[1])

print(sorted_count)

for k,v in sorted_count[:3]:
    print(k,end=" ")