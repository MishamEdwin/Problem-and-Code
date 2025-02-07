nums = [1, 2, 3, 3]

def containsDuplicate(arr):
    hashset=set()

    for elem in arr:
        if elem in hashset:
            return True
        else:
            hashset.add(elem)
    print(hashset)
    return False

print(containsDuplicate(nums))

