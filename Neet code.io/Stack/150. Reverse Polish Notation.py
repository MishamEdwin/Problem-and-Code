tokens = ["2", "1","+", "3", "*"]

stack=[]

for elem in tokens:
    if elem =="+":
        res=stack.pop()+stack.pop()
        stack.append(res)

    elif elem == "-":
        a,b=stack.pop(),stack.pop()
        res = b-a
        stack.append(res)

    elif elem =="*":
        res = stack.pop() * stack.pop()
        stack.append(res)

    elif elem == "/":
        a,b=stack.pop(),stack.pop()
        res=float(b)/a
        stack.append(int(res))

    else:
        res=int(elem)
        stack.append(res)

print(stack)
