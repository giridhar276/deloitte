# every class contains methods and variables 
class Employee:
    def getName(self,name):
        #self.name is accessible in all the methods
        self.name = name
    def displayName(self):
        print("Employee name :",self.name)

# object instantiation or object creation

emp1 = Employee()
emp1.getName("rita")
emp1.displayName()

emp2 = Employee()
emp2.getName("gita")
emp2.displayName()


emp3 = Employee()
emp3.getName("sita")
emp3.displayName()