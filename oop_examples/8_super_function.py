"""
Topic: super() Function
This example demonstrates super() function in Python with clear comments.
"""

"""
Topic: super() function
Use super() to access parent class methods or constructors.
"""

# Base class
class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Person name: {self.name}")

# Derived class
class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)   # Call base class constructor
        self.emp_id = emp_id

    def show(self):
        super().show()   # Call base class method
        print(f"Employee ID: {self.emp_id}")

# Create object
e1 = Employee("John", 102)
e1.show()