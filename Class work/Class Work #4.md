# Project: E-Commerce Shopping Cart

## Requirements

### 1. The Constructor (`__init__`)
* Create a class named `ShoppingCart`.
* The `__init__` method doesn't need any outside arguments besides `self`.
* Initialize an empty dictionary attribute called `items` (`{}`). 
  * *Note: The keys will be item names (strings), and the values will be their quantities (integers).*
* Initialize a dictionary attribute called `price_book` that maps item names to their floating-point prices. Use these starting products:
  * `"laptop"`: `999.99`
  * `"headphones"`: `149.99`
  * `"book"`: `14.99`

### 2. Method: `add_to_cart(self, item_name, quantity)`
* Adds a specified quantity of an item to the cart dictionary.
* **Logic:**
  * First, check if `item_name` exists in `self.price_book`. If it *doesn't*, print: `"Sorry, we do not sell [item_name]."`
  * If we do sell it, check if it's already in `self.items`. If it is, add the new `quantity` to the existing quantity. If it isn't, add it to `self.items` with a starting value of `quantity`.

### 3. Method: `calculate_total(self)`
* Calculates and returns the total cost of everything currently in the cart.
* **Logic:**
  * Initialize a variable `total = 0.0`.
  * Loop through the `self.items` dictionary. For each item, multiply its current quantity by its price from `self.price_book`, and add that amount to `total`.
  * Return the final `total` number.

---

## Test Code
Once you finish your class, copy this code to the bottom of your file to test your store logic in PyCharm:

```python
# Create a new shopping cart
cart = ShoppingCart()

# Test adding valid items
cart.add_to_cart("laptop", 1)
cart.add_to_cart("book", 2)
cart.add_to_cart("book", 1) # Duplicate item, should increase count to 3

# Test adding an invalid item
cart.add_to_cart("space_ship", 1)

print(f"Current Cart Items: {cart.items}")
# Expected output: {'laptop': 1, 'book': 3}

# Test total price calculation
final_price = cart.calculate_total()
print(f"Total Price: ${final_price:.2f}")
# Expected output: $1044.96