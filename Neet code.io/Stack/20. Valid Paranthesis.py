s = "()[]{}"

opening=["(","[","{"]


stack=[]
peek=-1

for elem in s:
    if elem in opening:
        stack.append(elem)

    else:
        if len(stack)==0:
            print("False")
            exit()
        if elem =="}" and stack[peek]=="{":
            stack.pop()
        elif elem == "]" and stack[peek]== "[":
            stack.pop()
        elif elem ==")" and stack[peek]== "(":
            stack.pop()

print(stack)

if len(stack)==0:
    print("True")
else:
    print("False")



