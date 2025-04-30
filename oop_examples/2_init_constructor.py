"""
Topic: __init__ Constructor Method
This example shows how the __init__ method initializes object attributes.
"""

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def show(self):
        print(f"Employee Name: {self.name}, ID: {self.emp_id}")

emp1 = Employee("Alice", 1001)
emp1.show()
