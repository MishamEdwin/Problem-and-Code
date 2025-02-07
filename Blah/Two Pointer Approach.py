#two pointer approach
arr=[1,2,3,4,5,6]
T=5

left=0
right=-1

for i in range(len(arr)):
    sum=arr[left]+arr[right]

    if(sum == T):
        print(arr[left],arr[right])
        exit()

    elif(sum<T):
        left+=1

    elif(sum>T):
        right-=1

""" #Normal approach
for i in range(len(arr)):
    for j in range(len(arr)):
        if (arr[i] + arr[j] == T):
            print(arr[i],arr[j])
            exit()
"""



