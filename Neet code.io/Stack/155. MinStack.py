Input=["MinStack", "push", 1, "push", 2,
       "push", 0, "getMin", "pop", "top", "getMin"]

class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self,val: int):
        self.stack.append(val)

    def top(self):
        peek = -1
        print(self.stack[peek])

    def pop(self):
        self.stack.pop()

    def getMin(self):
        print(min(self.stack))

    def display(self):
        print(self.stack)

minstack=MinStack()

minstack.display()
minstack.push(5)
minstack.push(6)
minstack.push(7)
minstack.push(8)
minstack.display()

minstack.top()

minstack.getMin()

minstack.pop()
minstack.display()










"""MinStack=[]

def push(val):
    MinStack.append(val)

def top():
    peek=-1
    print(MinStack[peek])

def pop():
    MinStack.pop()

def getMin():
    print(min(MinStack))
"""
