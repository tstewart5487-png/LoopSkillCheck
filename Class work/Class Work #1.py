class BankAccount:
    def __init__(self, owner, balance =0):
        self.bank_account_owner = owner
        self.bank_account_balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.bank_account_balance = self.bank_account_balance + amount
            print("Deposit Successful")
        else:
            print("Deposit Failed")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw Failed")
        elif amount > self.bank_account_balance:
            print("Insufficient Funds")
        else:
            self.bank_account_balance = self.bank_account_balance - amount
            print("Withdraw Successful")