
# every class contains methods and variables 
class Employee:
    def __init__(self,name,age,city):
        #self.name is accessible in all the methods
        self.name = name
        self.age = age 
        self.city = city
    def displayName(self):
        print("Employee name :",self.name)
        print("Employee age  :",self.age )
        print("Employee city :",self.city)

# object instantiation or object creation
emp1 = Employee("rita",25,"Hyd")
emp1.displayName()

emp2 = Employee("gita",30,"mum")
emp2.displayName()


emp3 = Employee("sita",40,"chennai")
emp3.displayName()