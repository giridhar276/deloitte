
# Create custom exception class
class LowBalanceError(Exception):
    def __init__(self, message="Balance too low"):
        self.message = message
        super().__init__(self.message)

# BankAccount class
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            # Raise custom exception if insufficient funds
            raise LowBalanceError("Cannot withdraw beyond available balance!")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: {self.balance}")

# Create account and withdraw funds
account = BankAccount(500)
account.withdraw(1000)  # Success

# Try withdrawing more than balance
try:
    account.withdraw(600)
except LowBalanceError as e:
    print(f"Error: {e}")

