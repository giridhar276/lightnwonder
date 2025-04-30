class Employee:
    # constructor
    def __init__(self,name):
        self.name = name
    def displayEmployee(self):
        print("Employee name:",self.name)

# condition is always True if this program is executed directly
if __name__ == "__main__":
    emp1 = Employee("rita")
    emp1.displayEmployee()

    emp2 = Employee("ram")
    emp2.displayEmployee()