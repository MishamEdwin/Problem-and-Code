class Vehicle:
    def Vehicle_display(self):
        print("This is a Vehicle Class")

class Fourwheeler:
    def Fourwheeler_display(self):
        print("This is a Four wheeler Class")

class Car(Vehicle,Fourwheeler): #Multiple Inheritance
    pass

car1=Car()

car1.Vehicle_display()
car1.Fourwheeler_display()