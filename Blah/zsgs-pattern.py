alps=[]
for i in range(65,91):
    elem=chr(i)
    alps.append(elem)

print(alps)

inp='M'

position=alps.index(inp)
print(position)

start=0
last=position

#top pattern
for i in range(1,position+1):
    for j in range(start, last+1):
        print(alps[j],end=" ")
    last = last - 1
    print()

#middle pattern
print(alps[0])

#bottom pattern
newlast=1

for i in range(1,position+1):
    for j in range(start,newlast+1):
        print(alps[j],end=" ")
    newlast+=1
    print()

