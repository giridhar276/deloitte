
## Abstraction :   Abstraction means hiding the details and showing only necessary parts(essential functionality)

from abc import ABC, abstractmethod
# ABC means abstract base class ... you cannot create an object for this class
# @abstractmethod : any class that inherits Vehicle must define start_engine
#                   It is used to declate a method that must be implemented by child classes

#ABC stards for abstract base class
# it is used to create a class that acts like blueprint or template for other classes

# Abstract class
# you cannot directly create objects if it has abstract methods
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass  # Force subclasses to implement this method

# Concrete class
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started!")

# Concrete class
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started!")

# Cannot instantiate Vehicle directly
# v = Vehicle()  # Error

car = Car()
bike = Bike()

car.start_engine()
bike.start_engine()
