str1 = "occurrence"
str2 = "car"
res=""

for elem in str1:
    if elem not in str2:
        res+=elem
print(res)