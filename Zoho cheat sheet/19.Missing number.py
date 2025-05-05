arr = [8, 2, 4, 5, 3, 7, 1]
arr.sort()
print(arr)

if len(arr)==0:
    print(1)
elif len(arr)==1:
    print(2)
else:
    for i in range(len(arr)):
        if i<len(arr)-1:
            if (arr[i] == arr[i+1]-1):
                continue
            else:
                print(arr[i+1]-1)
