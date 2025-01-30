"""
Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed the 
available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""

class Bank_account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"Deposited: T{money}. New balance: T{self.balance}")
        else:
            print("Invalid operation")
    
    def withdraw(self, money):
        if money > self.balance:
            print("Insufficient funds")
        elif money > 0:
            self.balance -= money
            print(f"Withdrawed: T{money}. New balance: T{self.balance}")
        else:
            print("Invalid operation")
    

me = Bank_account("Arnur", 5000)
me.deposit(1000)
me.withdraw(4000)
me.withdraw(1000000)
me.withdraw(-100)
me.deposit(-100)
