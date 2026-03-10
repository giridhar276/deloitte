

class Employee:
   'Common base class for all employees'
   empCount = 0   # class object (or) class variable # this variable will be shared across all objects

   def __init__(self, name, salary):
      self.name = name          # instance objects
      self.salary = salary
      Employee.empCount += 1    # shared variable
 

   def displayEmployee(self):
      """ this is my documentation of displayemployee"""
      print ("Name : ", self.name,  ", Salary: ", self.salary)

# if we execute this program directly , condition is always True
# condition becomes false if this program is imported to other program
if __name__ == "__main__":
    print (Employee.__doc__) 
    emp1 = Employee("Zara", 2000)
    emp2 = Employee("Manni", 5000)
    emp3 = Employee("Ram", 7000)
    emp1.displayEmployee()
    emp2.displayEmployee()
    emp3.displayEmployee()
    print (f"Total Employees {Employee.empCount}")
    