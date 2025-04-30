"""
Topic: Metaclasses and __new__ vs __init__
This example demonstrates metaclasses and __new__ vs __init__ in Python with clear comments.
"""

"""
Topic: Metaclasses and __new__ vs __init__
__new__ creates the instance (memory).
__init__ initializes the instance.
Metaclasses control class creation itself.
"""

# Define a metaclass
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class: {name}")
        return super().__new__(cls, name, bases, dct)

# Use metaclass in a class definition
class Person(metaclass=MyMeta):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

p = Person("Alice")
p.greet()

