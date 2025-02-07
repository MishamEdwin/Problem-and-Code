numbers = [1,2,3,4]
target = 5

l=0
r=len(numbers)-1

while l < r:
    summ=numbers[l]+numbers[r]

    if summ == target:
        print([l+1,r+1])
        break

    if summ > target:
        r-=1

    if summ < target:
        l+=1