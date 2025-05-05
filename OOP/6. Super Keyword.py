class Parent:
    def drive(self):
        print("Driving Skills")

    def game(self):
        print("Gaming Skills of Parent")

class Child(Parent):
    def game(self):
        super().game()
        

c1=Child()
c1.game()