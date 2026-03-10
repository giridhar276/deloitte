

# ---------------- single inheritance -------------------

# Parent class
class Animal:
    def sound(self):
        print("Animals make sound")

# Child class inheriting from Animal
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Create an instance of Dog
d = Dog()
d.sound()   # Inherited method from Animal
d.bark()    # Method from Dog

# ---------------- Multiple Inheritance ----------------

# First parent class
class Father:
    def skills(self):
        print("Father: gardening, carpentry")

# Second parent class
class Mother:
    def skills(self):
        print("Mother: painting, cooking")

# Child class inheriting from both Father and Mother
class Child(Father, Mother):
    def skills(self):
        Father.skills(self)   # Call Father's skills
        Mother.skills(self)   # Call Mother's skills
        print("Child: sports")

# Create instance
c = Child()
c.skills()
