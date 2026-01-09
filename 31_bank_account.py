''' Challenge: Bank Account

Objective: Build a class that manages a balance, implementing methods for deposits and withdrawals to simulate a real-world banking system. '''
class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = int(account_id)
        self.account_type = account_type
        self.pin = int(pin)
        self.balance = float(balance)

    def deposit(self, amount):
        self.balance += float(amount)
        return self.balance

    def withdraw(self, amount):
        amount = float(amount)
        if amount > self.balance:
            print("Insufficient funds.")
            return 0
        else:
            self.balance -= amount
            return amount

    def display_balance(self):
        print("Current Balance: $" + str(self.balance))

# Instantiate the account outside the class:
newbalance = BankAccount("han", "Doe", 1234, "Checking", 5678, 50.0)

# Use the methods with arguments:
newbalance.deposit(96)
withdrawn = newbalance.withdraw(25)
newbalance.display_balance()

print("Withdrawn: $" + str(withdrawn))
