



class CartItem:
    def __init__(self, item_name, price, quantity):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity

    # Human-readable print
    def __str__(self):
        return f"{self.item_name} - ₹{self.price} x {self.quantity}"

    # Add total value of two items
    def __add__(self, other):
        return (self.price * self.quantity) + (other.price * other.quantity)

    # len() returns quantity
    def __len__(self):
        return self.quantity


item1 = CartItem("Shoes", 2000, 2)
item2 = CartItem("Bag", 1500, 1)

print(item1)
print(item2)
print("Total cart value:", item1 + item2)
print("Quantity of first item:", len(item1))