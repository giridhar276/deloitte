


class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    # __str__ defines how the object is printed
    def __str__(self):
        return f"Book: {self.title} ({self.pages} pages)"

    # __add__ defines behavior of + operator between objects
    def __add__(self, other):
        return self.pages + other.pages

# Create two book objects
b1 = Book("Python Basics", 300)
b2 = Book("Advanced Python", 400)

print(b1)   # Calls __str__()
print(b2)   # Calls __str__()
print(f"Total pages: {b1 + b2}")  # Calls __add__()


