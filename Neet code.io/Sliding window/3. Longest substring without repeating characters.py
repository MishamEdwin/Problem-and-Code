s="zxyzxyz"

stack=[]
result=[]

for i in range(len(s)):
    temp=""
    for j in range(i,len(s)):
        temp+=s[j]
        stack.append(temp)
print(stack)

for elem in stack:
    if len(set(elem))== len(elem):
        result.append(elem)

result=(list(set(result)))

print(len(max(result)))
