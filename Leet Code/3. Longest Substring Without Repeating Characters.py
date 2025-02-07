s="pwwkew"

arr  = []
arr2 = []

res=0
restring=0

for i in range(len(s)):
    empty=""
    pointer=i

    while pointer<len(s):
        empty+=s[pointer]
        pointer+=1
        arr.append(empty)

print(arr)


for elem in arr:
    if len(set(elem)) == len(elem):
        arr2.append(elem)
print(arr2)
print(set(arr2))

arr2=set(arr2)
arr2=list(arr2)

print(arr2)

for elem in arr2:
    if res < len(elem):
        res=len(elem)
        restring=elem

print("res=",res,"restring=",restring)














"""
for right in range(len(s)):
    while (s[right] in stack):
        stack.remove(s[left])
        left += 1
    stack.append(s[right])
    res = max(res, right - left + 1)

print(res)
"""


"""
stack=[]

for i in s:
    if i not in stack:
        stack.append(i)
print(len(stack))
print(stack)"""
