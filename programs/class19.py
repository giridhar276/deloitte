


# Parent class
class Shape:
    def draw(self):
        print("Drawing a shape")

# Child class
class Circle:
    def draw(self):
        print("Drawing a circle")

# Another child class
class Square:
    def draw(self):
        print("Drawing a square")

# List of shapes
shapes = [Circle(), Square(), Shape()]

# Call draw method - behavior varies by object type
for shape in shapes:
    shape.draw()
    
    