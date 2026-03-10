
# static and class methods 


class Calculator:
    # Static method: utility function, does not use self or cls
    # A static method is a method that belongs to class .. but does not use object data ... does not use class data
    # simple helper function
    @staticmethod
    def add(x, y):
        return x + y

    # Class method: operates on the class itself
    # it is similar to how self refers to object
    # self------> current object        cls ---> current class
    @classmethod
    def greet(cls):
        print(f"Welcome to {cls.__name__}'s calculator!")

# Call static method directly (no object needed)
# this calls the static method directly using the class name 
# no object is created
result = Calculator.add(10, 5)
print(f"Addition Result: {result}")

# Call class method
# this calls the class method directly using class name
# no object is used
Calculator.greet()