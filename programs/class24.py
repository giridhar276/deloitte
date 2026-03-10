



from abc import ABC, abstractmethod

# Abstract class
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# Concrete class
class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


# Concrete class
class UPIPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


# Concrete class
class NetBankingPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Net Banking")


# Usage
p1 = CreditCardPayment()
p2 = UPIPayment()
p3 = NetBankingPayment()

p1.pay(2500)
p2.pay(1200)
p3.pay(5000)


