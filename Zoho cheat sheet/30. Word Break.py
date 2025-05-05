s =  "ilikegfg"
d= ["i", "like", "man", "india", "gfg"]
s2=""
ns=[]
for elem in d:
    s2+=elem

s=list(s)
s2=list(s2)

ptr1=0
ptr2=0

while ptr1<=len(s)-1 and ptr2<=len(s2)-1:
    if s[ptr1]==s2[ptr2]:
        ns.append(s2[ptr2])
        ptr1+=1
        ptr2+=1
    elif s[ptr1]!=s2[ptr2]:
        ptr2+=1


print(s)
print(ns)

if s==ns:
    print("True")
else:
    print("False")



