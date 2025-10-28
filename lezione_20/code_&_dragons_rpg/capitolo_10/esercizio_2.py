class BankAccount:
    def __init__(self, balance: float = 0) -> None:
        self.balance = balance

    
    def deposit(self, amount: float) ->None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise ValueError
        self.balance -= amount
        