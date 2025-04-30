"""
Topic: Instance Variables and Methods
Demonstrating how each object has its own copy of instance variables.
"""

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

dog1 = Dog("Buddy")
dog2 = Dog("Charlie")

dog1.bark()
dog2.bark()
