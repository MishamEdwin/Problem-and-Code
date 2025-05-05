arr=[10, 21, 22, 100, 101, 200, 300]
arr.sort()
print(arr)
count = 0

first=0
large=len(arr)-1 # largest val
last=large-1 # prev to the large value

while first<last:
    if arr[first]+arr[last] > arr[large]:
        count+=last-first
        last-=1
        large-=1
    else:
        first+=1

print(count)