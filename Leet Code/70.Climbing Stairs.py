n=5

front=1
back=1

for i in range(n-1):
    temp=front
    front=front+back
    back=temp

print(front)
