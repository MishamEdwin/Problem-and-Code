s="PROGRAM"
print(s)
mid=len(s)//2
print(mid)
newstring=s.split(s[mid])
print(newstring)
print(s[mid])
s2=s[mid]+newstring[1]+newstring[0]
print(s2)

pointer=0
blank=len(s2)

start=0
end=1

for i in range(len(s2)):
    print(" "*blank,end="")
    for j in range(start,end):
        print(s2[j],end="")
    print()
    end+=1
    blank-=1






"""
length=len(s)
mid=length//2

new_string=s[mid:]+s[:mid]
space=" "
spacelen=len(new_string)-1
start=0
end=0

for i in range(1,len(new_string)+1):
        end+=1
        print(space*spacelen,new_string[start:end])
        spacelen-=1
"""


