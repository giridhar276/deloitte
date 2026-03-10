



class Company:
    # Class variable (shared by all employees)
    company_name = "TechCorp"

    # Constructor (instance method)
    def __init__(self, name):
        self.name = name  # instance variable (specific to each employee)

    # Instance Method
    def show_employee(self):
        """
        Accesses instance (self) and class variable.
        """
        print(f"{self.name} works at {Company.company_name}")

    # Class Method
    @classmethod
    def rename_company(cls, new_name):
        """
        Accesses only the class (cls) — updates company name for ALL employees.
        """
        cls.company_name = new_name
        print(f"Company renamed to: {cls.company_name}")

    # Static Method
    @staticmethod
    def company_tagline():
        """
        Just prints a message — no access to self or cls.
        """
        print("Welcome! We build the future with code.")

# Create employee objects
emp1 = Company("Alice")
emp2 = Company("Bob")

# Instance Method (needs object)
emp1.show_employee()   # Alice works at TechCorp
emp2.show_employee()   # Bob works at TechCorp

# Static Method (utility function)
Company.company_tagline()  # Welcome! ...

# Class Method (change class-wide data)
Company.rename_company("InnoTech")

# See the effect on ALL employees
emp1.show_employee()   # Alice works at InnoTech
emp2.show_employee()   # Bob works at InnoTech


