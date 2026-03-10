
from abc import ABC, abstractmethod


# ============================================================
# ABSTRACTION
# ============================================================
# This is an abstract class.
# It acts like a template or blueprint.
# We cannot create objects directly from this class.
# Any child class must implement the calculate_interest method.
class Account(ABC):
    # Class variable
    # Shared by all objects of this class and its child classes
    bank_name = "ABC Bank"

    # CLASS METHOD
    # Works with the class itself, not object data
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
        print(f"Bank name changed to: {cls.bank_name}")

    # STATIC METHOD
    # Utility method - does not use self or cls
    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

    # Constructor
    def __init__(self, account_holder, balance):
        # Public instance variable
        self.account_holder = account_holder

        # ENCAPSULATION
        # Private variable using double underscore
        # It should not be accessed directly from outside
        self.__balance = balance

    # Getter method for private balance
    def get_balance(self):
        return self.__balance

    # Setter-like controlled method for deposit
    def deposit(self, amount):
        if Account.is_valid_amount(amount):
            self.__balance += amount
            print(f"{self.account_holder} deposited ₹{amount}")
        else:
            print("Invalid deposit amount")

    # Setter-like controlled method for withdraw
    def withdraw(self, amount):
        if not Account.is_valid_amount(amount):
            print("Invalid withdraw amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"{self.account_holder} withdrew ₹{amount}")

    # Magic method: controls how object is printed
    def __str__(self):
        return f"Bank: {self.bank_name}, Holder: {self.account_holder}, Balance: ₹{self.__balance}"

    # Magic method: defines + operator between two account objects
    def __add__(self, other):
        return self.get_balance() + other.get_balance()

    # ABSTRACT METHOD
    # Child classes must implement this method
    @abstractmethod
    def calculate_interest(self):
        pass


# ============================================================
# INHERITANCE
# SavingsAccount and CurrentAccount inherit from Account
# ============================================================

class SavingsAccount(Account):
    def __init__(self, account_holder, balance):
        # Reuse parent constructor
        super().__init__(account_holder, balance)

    # METHOD OVERRIDING
    # Child class provides its own version of calculate_interest
    def calculate_interest(self):
        interest = self.get_balance() * 0.05
        print(f"Savings Account Interest for {self.account_holder}: ₹{interest}")
        return interest

    # Additional method specific to SavingsAccount
    def account_type(self):
        print("This is a Savings Account")


class CurrentAccount(Account):
    def __init__(self, account_holder, balance):
        super().__init__(account_holder, balance)

    # METHOD OVERRIDING
    def calculate_interest(self):
        interest = self.get_balance() * 0.02
        print(f"Current Account Interest for {self.account_holder}: ₹{interest}")
        return interest

    # Additional method specific to CurrentAccount
    def account_type(self):
        print("This is a Current Account")


# ============================================================
# POLYMORPHISM
# Same method name behaves differently based on object type
# ============================================================
def show_interest(account):
    """
    This function accepts any object that has calculate_interest().
    This is polymorphism in action.
    """
    account.calculate_interest()


# ============================================================
# MAIN PROGRAM
# ============================================================

print("\n========== CREATE OBJECTS ==========")

# Object creation
acc1 = SavingsAccount("Giri", 50000)
acc2 = CurrentAccount("Ravi", 70000)

print("\n========== PRINT OBJECTS (__str__) ==========")
print(acc1)
print(acc2)

print("\n========== DEPOSIT AND WITHDRAW ==========")
acc1.deposit(5000)
acc1.withdraw(2000)

acc2.deposit(10000)
acc2.withdraw(15000)

print("\n========== CHECK UPDATED OBJECTS ==========")
print(acc1)
print(acc2)

print("\n========== ENCAPSULATION ==========")
# Access balance using getter method
print(f"{acc1.account_holder}'s balance: ₹{acc1.get_balance()}")
print(f"{acc2.account_holder}'s balance: ₹{acc2.get_balance()}")

# Direct access like acc1.__balance will not work properly
# because __balance is private

print("\n========== INHERITANCE ==========")
acc1.account_type()
acc2.account_type()

print("\n========== POLYMORPHISM ==========")
show_interest(acc1)   # SavingsAccount version
show_interest(acc2)   # CurrentAccount version

print("\n========== MAGIC METHOD: __add__ ==========")
total_balance = acc1 + acc2
print(f"Total balance of both accounts: ₹{total_balance}")

print("\n========== STATIC METHOD ==========")
print("Is 1000 a valid amount?", Account.is_valid_amount(1000))
print("Is -50 a valid amount?", Account.is_valid_amount(-50))

print("\n========== CLASS METHOD ==========")
print("Old Bank Name:", Account.bank_name)
Account.change_bank_name("Future Secure Bank")
print("New Bank Name in acc1:", acc1.bank_name)
print("New Bank Name in acc2:", acc2.bank_name)

print("\n========== FINAL OBJECT DETAILS ==========")
print(acc1)
print(acc2)


###############################