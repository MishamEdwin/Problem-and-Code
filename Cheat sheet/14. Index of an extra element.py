arr1=[3,5,7,8,11,13]
arr2=[3,5,7,11,13]

ptr=0

for elem in arr1:
    if ptr < len(arr2):
        if elem == arr2[ptr]:
            ptr+=1
        else:
            print(elem,arr1.index(elem))
