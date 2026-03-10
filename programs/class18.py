


# Base class
class AccountHolder:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Account Holder Name: {self.name}")


# Derived class
class BankCustomer(AccountHolder):
    def __init__(self, name, account_number):
        super().__init__(name)   # Call base class constructor
        self.account_number = account_number

    def show(self):
        super().show()   # Call base class method
        print(f"Account Number: {self.account_number}")


# Create object
c1 = BankCustomer("Ravi", 56789)
c1.show()