# Exercise 1: The Bank Account (Beginner)

## Goal
Create a class that tracks a monetary balance and handles basic financial operations.

## Requirements
*   Class named `BankAccount`.
*   `__init__` method accepting `owner` and an optional starting `balance` (defaulting to 0).
*   Method `deposit(amount)` that adds money to the balance.
*   Method `withdraw(amount)` that subtracts money only if funds are sufficient, otherwise printing an error.

---

*Scroll down to see the solution...*

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

## Solution

Here is the implementation of the `BankAccount` class following your exact specifications:

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print(f"Error: Insufficient funds. Available balance: ${self.balance}")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")

# Example Usage:
if __name__ == "__main__":
    # Create an account for Alice with a starting balance of $100
    alice_account = BankAccount("Alice", 100)
    
    # Check initial balance
    print(f"Account Owner: {alice_account.owner}")
    print(f"Initial Balance: ${alice_account.balance}")
    
    # Deposit money
    alice_account.deposit(50)
    print(f"New Balance: ${alice_account.balance}")
    
    # Try to withdraw more money than available
    alice_account.withdraw(200)
    
    # Successfully withdraw money
    alice_account.withdraw(40)
    print(f"Final Balance: ${alice_account.balance}")