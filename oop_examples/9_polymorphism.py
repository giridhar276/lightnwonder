"""
Topic: Polymorphism and Method Overriding
This example demonstrates polymorphism and method overriding in Python with clear comments.
"""

# Parent class
class Shape:
    def draw(self):
        print("Drawing a shape")

# Child class
class Circle:
    def draw(self):
        print("Drawing a circle")

# Another child class
class Square:
    def draw(self):
        print("Drawing a square")

# List of shapes
shapes = [Circle(), Square(), Shape()]

# Call draw method - behavior varies by object type
for shape in shapes:
    shape.draw()