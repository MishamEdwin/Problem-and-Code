pattern="abba"
s="dog cat cat dog"

d=dict()
print(d)

l=s.split(' ')
print(l)

if len(pattern)!=len(l):
    print("Not a pattern")

set1=set(pattern)
print(set1)

if len(set(pattern)) !=len(l):
    print("Not a pattern")

for i in range(len(l)):
    if l[i] not in d:
        d[l[i]]=pattern[i]
    elif d[l[i]] != pattern[i]:
        print("Not a pattern")

