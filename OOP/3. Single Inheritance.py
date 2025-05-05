class Vehicle:  # Base Class

    def Vehicle_display(self):
        print("This is Vehicle Class")

class Bike(Vehicle):  # Derived Class

    def Bike_display(self):
        print("Bike is a Vehicle")


b1=Bike()
b1.Vehicle_display()
b1.Bike_display()