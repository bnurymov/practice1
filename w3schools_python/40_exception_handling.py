# Python Exception Handling (Advanced)

# Custom exception
class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(f"Cannot withdraw {amount}, balance is {balance}")

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(amount, self.balance)
        self.balance -= amount
        return self.balance

account = BankAccount(100)

try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(f"Error: {e}")
else:
    print("Withdrawal successful")
finally:
    print(f"Current balance: {account.balance}")
