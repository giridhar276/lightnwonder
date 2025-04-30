"""
Topic: Abstraction and Abstract Base Classes
This example demonstrates abstraction and abstract base classes in Python with clear comments.

What is Abstraction in simple terms?
Abstraction means hiding the details and showing only the necessary parts.

"You don’t need to know how the engine works, just know you can start it."
ABC: Means "Abstract Base Class". You cannot create an object of this class.

@abstractmethod: Any class that inherits Vehicle must define start_engine.
Vehicle like a template 

"""

from abc import ABC, abstractmethod

# Abstract class
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