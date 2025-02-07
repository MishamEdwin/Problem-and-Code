s = "cbbd"

arr=[]
palindrome=[]

res=0
restring=""

for i in range(len(s)):
    empty=""
    pointer = i

    while pointer < len(s):
        empty+=s[pointer]
        arr.append(empty)
        pointer+=1

print(arr)

print(len(arr))

for elem in arr:
    if elem == elem[::-1]:
        palindrome.append(elem)

print(palindrome)

for elem in palindrome:
    if res<len(elem):
        res=len(elem)
        restring=elem

print("res=",res,"restring=",restring)


