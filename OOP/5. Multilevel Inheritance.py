class Vehicle:                         # Grand Parent
    def Vehicle_display(self):
        print("This is a Vehicle Class")

class Fourwheeler(Vehicle):            # Parent
    def Fourwheeler_display(self):
        print("This is a Four wheeler Class")

class Car(Fourwheeler): # Multilevel Inheritance -- Child
    def Car_display(self):
        print("This is a Car Class")

f1=Fourwheeler()
f1.Fourwheeler_display()
f1.Vehicle_display()

c1=Car()
c1.Fourwheeler_display()
c1.Vehicle_display()
c1.Vehicle_display()