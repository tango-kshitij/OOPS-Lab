class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.transaction_history = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            return f"Deposited: ${amount}. New balance: ${self.balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            return f"Withdrew: ${amount}. New balance: ${self.balance}"
        elif amount > self.balance:
            return "Insufficient balance."
        else:
            return "Withdrawal amount must be positive."

    def view_transaction_history(self):
        if not self.transaction_history:
            return "No transactions yet."
        return "\n".join(self.transaction_history)


atm = ATM(1000) 

print(atm.check_balance())
print(atm.deposit(500))
print(atm.withdraw(200))
print(atm.view_transaction_history()) 
