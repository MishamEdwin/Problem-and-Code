from abc import ABC,abstractmethod

class Vehicle(ABC):       # Abstract Class

    @abstractmethod
    def Engine_Start(self):    # Abstract Method aka Pure Virtual Function
        print("Vehicle is ON")

class Bike(Vehicle):

    def Engine_Start(self):
        print("Bike Engine is ON")

class Car(Vehicle):

    def Engine_Start(self):
        print("Car Engine is ON")

# v1=Vehicle()
# v1.Engine_Start()  Can't use this because it's a virtual function

b1=Bike()
b1.Engine_Start()

c1=Car()
c1.Engine_Start()
