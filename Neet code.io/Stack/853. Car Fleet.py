target = 10
position = [4,1,0,7]
speed = [2,2,1,1]

time_stack=[]
fleet=len(position)

# creating hashmap of position and speed
hashmap={}
for i in range(len(position)):
    hashmap[position[i]]=speed[i]
print(hashmap)

#sorting the hashmap according to the position i.e key
hashmap=dict(sorted(hashmap.items()))
print(hashmap)

#creating a stack of (key,val) sets
stack=[]
for elem in hashmap:
    stack.append((elem, hashmap[elem]))
print(stack)


#calculating time for each pos/cars
for elem in stack:
    pos=elem[0]
    spd=elem[1]

    distance=target-pos

    time=distance/spd
    time_stack.append(time)
print(time_stack)

#grouping the fleet
for i in range(len(time_stack)-1,-1,-1):
    if i > 0:
        #print(time_stack[i],time_stack[i-1])
        if (time_stack[i]>time_stack[i-1]) or (time_stack[i] == time_stack[i-1]):
            fleet-=1

print(fleet)
