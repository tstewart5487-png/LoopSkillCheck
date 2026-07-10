class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.price_book = {
            "laptop": 999.99,
            "headphones": 149.99,
            "book": 14.99
        }

    def add_to_cart(self, item_name, quantity):
        if item_name not in self.price_book:
            print(f"Sorry, we do not sell {item_name}")
        elif item_name in self.price_book:
            if item_name in self.items:
                self.items[item_name] = self.items[item_name] + quantity
            else:
                self.items[item_name] = quantity

    def calculate_total(self):
        total = 0.00
        for item in self.items:
            total = total + self.price_book[item] * self.items[item]
        return total
cart = ShoppingCart()
cart.add_to_cart("laptop", 1)
cart.add_to_cart("book", 2)
cart.add_to_cart("headphones", 3)
cart.add_to_cart("space_ship", 3)

print(cart.items)

final_price = cart.calculate_total()
print(f"Total Price: ${final_price}")