


# Base class
class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 1000

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.account_holder} deposited ${amount}")
        print(f"Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.account_holder} withdrew ${amount}")
        else:
            print("Insufficient balance")
        print(f"Balance: ${self.balance}")

# Child class 1
class SavingsAccount(BankAccount):
    def add_interest(self):
        interest = self.balance * 0.05
        self.balance += interest
        print(f"Interest added: ${interest}")
        print(f"Updated Balance: ${self.balance}")

# Child class 2
class CurrentAccount(BankAccount):
    def overdraft(self):
        self.balance += 500
        print("Overdraft facility used: $500 added")
        print(f"Updated Balance: ${self.balance}")

# Usage
print("\n--- Hierarchical Inheritance Example (Banking) ---")

savings_user = SavingsAccount("Diana")
savings_user.deposit(500)
savings_user.add_interest()

current_user = CurrentAccount("Ethan")
current_user.withdraw(300)
current_user.overdraft()
