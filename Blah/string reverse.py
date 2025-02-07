s="racecar"
pointer=-1
reverse=""
for i in range(len(s)):
    reverse+=s[pointer]
    pointer-=1
print(s,reverse)
