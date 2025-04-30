"""
Topic: Classes and Objects
This example demonstrates how to create and use classes and objects in Python.
"""

# Define a class
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # instance variable
        self.model = model  # instance variable

    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")

# Create objects (instances)
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Access methods
car1.display_info()
car2.display_info()
