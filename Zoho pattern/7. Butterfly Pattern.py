N=5
space=N*2-2
star=1
#top
for i in range(N-1):
    print("*"*star + " "*space + "*"*star)
    star+=1
    space-=2
#mid
print("*"*(star*2))
print("*"*(star*2))

# print(star)
# print(space)

star-=1
space+=2

#bottom

for i in range(N-1):
    print("*"*star + " "*space + "*"*star)
    star-=1
    space+=2