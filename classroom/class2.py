



class Employee:
    def getEmployee(self,name):
        self.name = name
    def displayEmployee(self):
        print("Employee name:",self.name)
        
if __name__ == "__main__":
    emp1 = Employee()
    emp1.getEmployee("rita")
    emp1.displayEmployee()

    emp2 = Employee()
    emp2.getEmployee("ram")
    emp2.displayEmployee()