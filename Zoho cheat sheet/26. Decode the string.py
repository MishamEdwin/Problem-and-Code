s = "3[b2[ca]]"
stack = []

for char in s:
    if char != "]":
        stack.append(char)
    else:
        res = ""
        while stack[-1] != "[":
            res = stack.pop() + res  # Extract characters inside brackets
        stack.pop()  # Remove '['

        num = ""
        while stack and stack[-1].isdigit():
            num = stack.pop() + num  # Extract number
        stack.append(res * int(num))  # Repeat and push back

print("".join(stack))  # Join stack into a string
