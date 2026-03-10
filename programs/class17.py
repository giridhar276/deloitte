

### multiple 
# Base class 1
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


# Base class 2
class RewardProgram:
    def __init__(self):
        self.reward_points = 0

    def add_points(self, points):
        self.reward_points += points
        print(f"Reward Points Added: {points}")
        print(f"Total Reward Points: {self.reward_points}")


# Derived class using multiple inheritance
class PremiumBankAccount(BankAccount, RewardProgram):
    def __init__(self, account_holder):
        BankAccount.__init__(self, account_holder)
        RewardProgram.__init__(self)

    def deposit(self, amount):
        print("Premium Account Deposit Processing...")
        super().deposit(amount)
        self.add_points(10)


# Usage
print("\n--- Multiple Inheritance Example (Banking) ---")
customer = PremiumBankAccount("Bob")
customer.deposit(500)
customer.deposit(300)
customer.withdraw(200)