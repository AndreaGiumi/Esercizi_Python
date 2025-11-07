class Account:
    def __init__(self, account_id: str, balance: float) -> None:

        self.account_id = account_id
        self.balance = balance
    
    def deposit(self, amount: float) -> None:
        if amount >= 0:
            self.balance += amount
    def get_balance(self) -> str:
        return self.balance
    

class Bank:
    def __init__(self):
        self.accounts: dict[str, Account] = {}
    
    def create_account(self, account_id: str) -> dict | str:
        if account_id in self.accounts:
            raise KeyError( "Account with this ID already exists")
        self.accounts[account_id] = 0

        return self.accounts[account_id]
    
    def deposit(self, account_id: str, amount: float) -> None:
        if account_id not in self.accounts:
            raise KeyError("Account with this ID doesn't exists")
        self.accounts[account_id] += amount

    def get_balance(self, account_id: str) -> str:
        if account_id not in self.accounts:
            raise KeyError("Account not found")
        return self.accounts[account_id]

