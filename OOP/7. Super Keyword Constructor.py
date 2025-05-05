class Parent:
    def __init__(self,Networth):
        self.Networth=Networth

class Child(Parent):
    def __init__(self,Networth):
        super().__init__(Networth//2)


p1=Parent(5000000)
print(p1.Networth)
c1=Child(120000)
print(c1.Networth)
