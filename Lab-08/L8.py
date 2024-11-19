class TransactionHistory:
    def __init__(self):
        self.history = []

    def add_transaction(self, transaction):
        self.history.append(transaction)

    def show_history(self):
        if not self.history:
            return "No transactions available."
        return "\n".join(self.history)


class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.transaction_history = TransactionHistory()

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.add_transaction(f"Deposited: ${amount}")
            return f"Deposited: ${amount}. New balance: ${self.balance}"
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self.balance:
            return "Insufficient balance."
        self.balance -= amount
        self.transaction_history.add_transaction(f"Withdrew: ${amount}")
        return f"Withdrew: ${amount}. New balance: ${self.balance}"

    def show_history(self):
        return self.transaction_history.show_history()


class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance."
        if amount > 5000:
            return "Withdrawal limit exceeded for savings account."
        self.balance -= amount
        self.transaction_history.add_transaction(f"Withdrew: ${amount} from Savings Account")
        return f"Withdrew: ${amount}. New balance: ${self.balance}"


class CurrentAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=1000):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > (self.balance + self.overdraft_limit):
            return "Withdrawal limit exceeded for current account."
        self.balance -= amount
        self.transaction_history.add_transaction(f"Withdrew: ${amount} from Current Account")
        return f"Withdrew: ${amount}. New balance: ${self.balance}"


class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, transaction_limit=10000):
        super().__init__(account_number, account_holder, balance)
        self.transaction_limit = transaction_limit

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self.transaction_limit:
            return "Transaction limit exceeded for checking account."
        if amount > self.balance:
            return "Insufficient balance."
        self.balance -= amount
        self.transaction_history.add_transaction(f"Withdrew: ${amount} from Checking Account")
        return f"Withdrew: ${amount}. New balance: ${self.balance}"


savings = SavingsAccount("SA12345", "Alice", 2000)
current = CurrentAccount("CA12345", "Bob", 5000)
checking = CheckingAccount("CK12345", "Charlie", 10000)

print(savings.deposit(500))
print(savings.withdraw(3000))
print(savings.show_history())

print(current.deposit(2000))
print(current.withdraw(6000))
print(current.show_history())

print(checking.withdraw(5000))
print(checking.show_history())
