#Input: s="tree"
#Output: "eert"

s="tree"

dictionary={}

#creating k:v pairs
for char in s:
    if char not in dictionary:
        dictionary[char]=1
    else:
        dictionary[char]+=1

print(dictionary)


#creating a list of (k:v) tuples
count_list=[]

for char in dictionary:
    count_list.append((char,dictionary[char]))

print(count_list)

#sort the list based on frequency and descending order
#combinations  (key=lambda x: (x[1],x[0])) or (key=lambda x: (-x[1],x[0]),reverse=True)
count_list.sort(key=lambda x: (-x[1],x[0]))

print(count_list)

for char,count in count_list:
    print((char +'') * count, end="")