


class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def __str__(self):
        return f"Account Holder: {self.holder}, Balance: ₹{self.balance}"

    def __add__(self, other):
        return self.balance + other.balance


a1 = BankAccount("Giri", 25000)
a2 = BankAccount("Rahul", 40000)

print(a1)
print(a2)
print("Total Balance:", a1 + a2)
