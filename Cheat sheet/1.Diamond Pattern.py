n=6
blank=n

start=0
end=1

#top
for i in range(n):
    print(" " * blank, end="")
    blank-=1

    for j in range(start,end):
        print("*",end=" ")
    end+=1
    print()


end-=1
blank+=1

#bottom
for i in range(n):
    print(" " * blank, end="")
    blank+=1

    for j in range(start,end):
        print("*",end=" ")
    end-=1
    print()