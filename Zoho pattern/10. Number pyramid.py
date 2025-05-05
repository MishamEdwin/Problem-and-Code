N=6
num=[]
for i in range(N-1,-N,-1):
    num.append(abs(i))
# print(num)

space=N-1
mid=len(num)//2


first=mid
last=mid

for i in range(N):
    print(" "*space,end="")
    space-=1

    if first==last:  # first line
        print(str(num[last]))
        first-=1
        last+=1
    else:          # rest of the lines
        for j in range(first, last + 1):
            print(num[j], end="")
        print()
        first -= 1
        last += 1

