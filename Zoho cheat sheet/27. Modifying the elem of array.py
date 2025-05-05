arr= [2, 2, 0, 4, 0, 8]

for i in range(len(arr)-1):
    if arr[i]>0 and arr[i+1]>0:
        if arr[i]==arr[i+1]:
            arr[i]*=2
            arr[i+1]=0

print(arr)

ptr=0
for i in range(1,len(arr)):
    if arr[ptr]==0:
        if arr[i]>0:
            arr[ptr] = arr[i]
            arr[i] = 0
            ptr += 1
    else:
        ptr+=1

print(arr)

# mod=[0]*len(arr)
# ptr=0
# for i in range(len(arr)):
#     if arr[i]>0:
#         mod[ptr]=arr[i]
#         ptr+=1
# print(mod)