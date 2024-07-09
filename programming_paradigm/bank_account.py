# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.account_balance:
                self.account_balance -= amount
                return True
            else:
                return False
        else:
            print("Invalid withdrawal amount.")
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
