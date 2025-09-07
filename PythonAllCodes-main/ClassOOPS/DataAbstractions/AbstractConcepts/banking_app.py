# Small Banking Application
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False
    def __str__(self):
        return f"Account({self.owner}, Balance: {self.balance})"

acc = Account("Suraj", 1000)
acc.deposit(500)
print(acc)
acc.withdraw(300)
print(acc)
