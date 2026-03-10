


class Bank:
    bank_name = "National Trust Bank"  # Class variable shared across all accounts

    def __init__(self, account_holder):
        self.account_holder = account_holder  # Instance variable

    @classmethod
    def change_bank_name(cls, new_name):
        """Change the name of the bank"""
        cls.bank_name = new_name

    def show_account_info(self):
        """Display account holder and bank information"""
        print(f"Account Holder: {self.account_holder}, Bank: {self.bank_name}")

# Create account holders
account1 = Bank("Alice")
account2 = Bank("Bob")

# Show initial bank information
account1.show_account_info()
account2.show_account_info()

# Change the bank name
Bank.change_bank_name("Global Finance Bank")

# Show updated bank information
account1.show_account_info()
account2.show_account_info()
