"""
Topic: Encapsulation with Getters and Setters
This example demonstrates encapsulation with getters and setters in Python with clear comments.
"""

class Student:
    def __init__(self, name, grade):
        self.__name = name    # Private variable
        self.__grade = grade  # Private variable

    # Getter method for grade
    #@property turns a method into an attribute.
    #Now, you can access the student's grade like a normal variable: s1.grade instead of s1.grade().
    #It simply returns the value of the private variable __grade.
    @property
    def grade(self):
        return self.__grade

    # Setter method for grade with validation
    #@grade.setter allows you to set or update the grade safely.
    #It checks if the new grade is between 0 and 100.
    #If yes, it updates self.__grade.
    #If not, it shows an error message and does not update the grade.
    @grade.setter
    def grade(self, value):
        if 0 <= value <= 100:
            self.__grade = value
        else:
            print("Invalid grade! Must be between 0 and 100.")

    # Method to display student info
    def display(self):
        print(f"Student: {self.__name}, Grade: {self.__grade}")


# Create a Student object
s1 = Student("Tom", 85)
s1.display()

# Modify grade correctly
s1.grade = 95
s1.display()

# Attempt to set invalid grade
s1.grade = 150