import math

arr= [2, 3, -8, 7, -1, 2, 3]

cur_sum=0
max_sum=-math.inf # Negative Infinity

for i in range(len(arr)):
    temp=cur_sum+arr[i]

    if temp<arr[i]:
        cur_sum=arr[i]

    else:
        cur_sum=temp

    if max_sum < cur_sum:
        max_sum=cur_sum

print(max_sum)


# Brute Force
# sub_arrays=[]
# new_subs=[]
#
# max_Sum=0
# max_arr=[]
#
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         sub_arrays.append(arr[i:j+1])
#
# # print(sub_arrays)
#
# for subs in sub_arrays:
#     if subs in new_subs:
#         continue
#     else:
#         new_subs.append(subs)
#
# print(new_subs)
#
# for elem in new_subs:
#     if sum(elem)>max_Sum:
#         max_Sum=sum(elem)
#         max_arr=elem
#
# print(max_Sum)
# print(max_arr)