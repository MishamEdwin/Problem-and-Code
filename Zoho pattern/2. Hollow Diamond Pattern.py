n=9
count=n+1

#first
print("* "*count)
#top
temp=n//2
blank=1
for i in range(n//2):
    print("* "*temp,"  "*blank,"* "*temp)
    temp-=1
    blank+=2

temp+=2
blank-=4

#bottom
for i in range(n//2 -1): #runs 4 times
    print("* "*temp,"  "*blank,"* "*temp)
    temp+=1
    blank-=2
# last
print("* "*count)
