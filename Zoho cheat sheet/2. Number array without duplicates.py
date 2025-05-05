nums = [111, 222, 333, 4444, 666]

newarr=[]

for elem in nums:
    for digit in str(elem):
        if digit not in newarr:
            newarr.append(digit)


print(newarr)

for i in newarr:
    print(i,end=" ")







