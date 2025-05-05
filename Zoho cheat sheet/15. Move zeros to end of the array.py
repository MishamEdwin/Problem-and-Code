arr= [0, 0, 0, 4]
new_arr=[0]*len(arr)
front=0


print(front)
print(arr)
print(new_arr)

for elem in arr:
    if front<len(arr):
        if elem >0:
            new_arr[front]=elem
            front+=1

print(arr)
print(new_arr)
