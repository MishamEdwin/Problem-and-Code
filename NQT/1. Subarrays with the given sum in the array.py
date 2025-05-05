arr=[3,4,-7,1,3,3,1,-4]
target=7
sub_arrays=[]

#two pointer approach
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        sub_arrays.append(arr[i:j+1]) #array index slicing

#print(sub_arrays)

#removing the duplicates
new_sub=[]
for subs in sub_arrays:
    if subs in new_sub:
        continue
    else:
        new_sub.append(subs)

#finding the target subarrays
op=[]
for subs in new_sub:
    if sum(subs) == target:
        op.append(subs)
    else:
        continue

print(op)


# arr = [3, 4, -7, 1, 3, 3, 1, -4]
# target = 7
# sub_arrays = []
#
# left = 0
# window_sum = 0
#
# for right in range(len(arr)):
#     window_sum += arr[right]  # Expand the window
#
#     # Shrink window if sum exceeds target
#     while window_sum > target and left <= right:
#         window_sum -= arr[left]
#         left += 1
#
#     # If sum matches target, store the subarray
#     if window_sum == target:
#         sub_arrays.append(arr[left:right+1])
#
# print(sub_arrays)

