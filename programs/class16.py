



#### multilevel inheritance 

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


# First-level derived class
class SavingsAccount(BankAccount):
    def add_interest(self):
        interest = self.balance * 0.05
        self.balance += interest
        print(f"Interest added: ${interest}")
        print(f"New Balance: ${self.balance}")


# Second-level derived class
class PremiumSavingsAccount(SavingsAccount):
    def cashback_reward(self):
        cashback = 200
        self.balance += cashback
        print("Cashback reward credited!")
        print(f"Reward Amount: ${cashback}")
        print(f"Updated Balance: ${self.balance}")


# Usage
print("\n--- Multilevel Inheritance Example (Banking) ---")
customer = PremiumSavingsAccount("Carol")
customer.deposit(500)
customer.withdraw(200)
customer.add_interest()
customer.cashback_reward()