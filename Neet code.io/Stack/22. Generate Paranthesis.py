n=0
stack=[]
res=[]

def backtrack(openCount,closeCount):

    if openCount == closeCount == n: #Base Condition
        res.append("".join(stack))
        return

    if openCount > closeCount:
        stack.append(")")
        backtrack(openCount,closeCount+1) #Recursive Calling
        stack.pop()# This line is used in this program to backtrack — it allows the program
                   # to undo the last choice and try other possible choices.


    if openCount < n:
        stack.append("(")
        backtrack(openCount+1,closeCount) #Recursive Calling
        stack.pop()# This line is used in this program to backtrack — it allows the program
                   # to undo the last choice and try other possible choices.

    return res

print(backtrack(0,0))
