'''
You want to change the value of the class variable school_name.

This change should reflect across all existing and future instances of the class.

A @classmethod operates on the class itself, not on any individual instance.

It takes cls (the class) as its first argument instead of self (the instance).

Use @classmethod when you want to change or access class variables — variables that are shared by all instances.

Without @classmethod, you'd be modifying the variable for only one instance, not the whole class.

 What is cls?
cls is just a name, not a keyword in Python.

It refers to the class itself (like self refers to the instance).

It's not fixed — you could technically call it anything, but cls is the widely accepted convention.


'''

class School:
    school_name = "Green Valley High"

    def __init__(self, student_name):
        self.student_name = student_name

    @classmethod
    def change_school_name(cls, name):
        cls.school_name = name

student1 = School("John")
student2 = School("Jane")

print(student1.school_name)
print(student2.school_name)

School.change_school_name("Blue Ridge High")

print(student1.school_name)
print(student2.school_name)