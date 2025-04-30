"""
Topic: Static and Class Methods
This example demonstrates static and class methods in Python with clear comments.
"""

class Calculator:
    # Static method: utility function, does not use self or cls
    @staticmethod
    def add(x, y):
        return x + y

    # Class method: operates on the class itself
    @classmethod
    def greet(cls):
        print(f"Welcome to {cls.__name__}'s calculator!")

# Call static method directly (no object needed)
result = Calculator.add(10, 5)
print(f"Addition Result: {result}")

# Call class method
Calculator.greet()