import math
def median(a,b):
    nums1=a
    nums2=b
    sum = []
    for elem in nums1:
        sum.append(elem)

    for elem in nums2:
        sum.append(elem)

    sum = sorted(sum)
    print(sum)

    print("length=", len(sum))
    length = len(sum)

    if length % 2 != 0:
        mid = math.ceil(length / 2)
        return mid

    elif length % 2 == 0:
        mid1 = length / 2
        mid2 = (length / 2) + 1
        sol = (mid1 + mid2) / 2
        return sol

a = [1,3,5,9]
b = [2,4,6,7]
print(median(a,b))