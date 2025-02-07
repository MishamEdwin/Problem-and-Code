n=5
blanks=n
alphs=[]
start=0
end=1

for i in range(65,91):
    alphs.append(chr(i))

rows=n

for i in range(rows):
    print(" " * blanks,end="")
    blanks-=1

    for j in range(start,end):
        print(alphs[j],end=" ")
    print()
    end += 1


