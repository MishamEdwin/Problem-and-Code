N=6
blank=0

first=0
last=N*2-1
for i in range(N):
    print(" "*blank, end="")
    blank+=1

    for j in range(first,last):
        print("*",end="")
    last-=2
    print()