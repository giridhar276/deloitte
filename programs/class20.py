


# Parent class
class BankAccount:
    def transaction(self):
        print("Bank account performs a basic transaction")

# Child class: SavingsAccount
class SavingsAccount(BankAccount):
    def transaction(self):
        print("Savings account earns interest on balance")

# Child class: CurrentAccount
class CurrentAccount(BankAccount):
    def transaction(self):
        print("Current account allows frequent business transactions")

# Child class: LoanAccount
class LoanAccount(BankAccount):
    def transaction(self):
        print("Loan account processes EMI payment")

# Create different account types
accounts = [SavingsAccount(), CurrentAccount(), LoanAccount(), BankAccount()]

# Each account performs its own transaction
for acc in accounts:
    acc.transaction()