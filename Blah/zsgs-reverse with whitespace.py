inp="rock and"

pointer=-1

reverse=""

for i in range(len(inp)):
    reverse+=inp[pointer]
    pointer-=1
print(reverse)