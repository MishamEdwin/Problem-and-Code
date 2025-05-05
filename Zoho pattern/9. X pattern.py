s=input()

in_space=len(s)-2
out_space=0

first=0
last=-1

#top
for i in range(len(s)//2):
    print(" "*out_space + s[first] + " " *in_space + s[last])
    out_space+=1
    first+=1
    in_space-=2
    last-=1

#mid
print(" "*(len(s)//2) +s[len(s)//2])

#bottom
first-=1
last+=1
out_space-=1
in_space+=2

for i in range(len(s)//2):
    print(" "*out_space + s[first] + " "*in_space + s[last])
    out_space-=1
    first-=1
    in_space+=2
    last+=1