n=5

first=0
last=1

count=n
blank=chr(32)

#Top
for i in range(n):          # outer loop to print the blank space
    print(blank * count,end="")
    count-=1

    for j in range(first,last): # inner loop to print the character
        print("* ",end="")
    print()               # line break
    last+=1               # incrementing the range

count+=2                 # Increase the count to +2 for 2 blank space
last-=2                  # Decrease the last to -2 for reducing the char range

# Bottom

for i in range(n):
    print(blank*count,end="")
    count+=1

    for j in range(first,last):
        print("* ",end="")
    print()
    last-=1















# n=6
# blank=n
#
# start=0
# end=1
#
# #top
# for i in range(n):
#     print(" " * blank, end="")
#     blank-=1
#
#     for j in range(start,end):
#         print("*",end=" ")
#     end+=1
#     print()
#
#
# end-=1
# blank+=1
#
# #bottom
# for i in range(n):
#     print(" " * blank, end="")
#     blank+=1
#
#     for j in range(start,end):
#         print("*",end=" ")
#     end-=1
#     print()