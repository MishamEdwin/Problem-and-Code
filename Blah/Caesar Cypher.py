s="Caesar Cipher"
val=2

def Caesar(s,val):
    int_arr = []
    new_arr = []
    new_s = ""
    print(s)
    for elem in s:
        elem = ord(elem)
        int_arr.append(elem)
    print(int_arr)

    for nums in int_arr:
        if nums == 32:
            new_arr.append(nums)
        else:
            nums += val
            new_arr.append(nums)

    print(new_arr)

    for i in new_arr:
        alp = chr(i)
        new_s += alp

    print(new_s)

Caesar(s,val)