class BankAccount:
    bank_name : str = "Python Bank"

    total_accounts : int = 0

    def __init__(self,account_number : str,balance : float = 0):
        self.account_number = account_number
        self.balance= balance
        BankAccount.total_accounts += 1

    def deposit(self, amount : float):
          self.balance += amount
          return self.balance

    def withdraw(self, amount) -> bool:
        if self.balance < amount:
            return False
        else:
            self.balance = self.balance - amount
            return True

    def get_balance(self)->float :
        return self.balance

if __name__=="__main__":
    acc1 = BankAccount("ACC001", 1000)
    acc2 = BankAccount("ACC002")
    print(acc1.deposit(500))  # Should work
    print(acc1.withdraw(2000))  # Should return False
    print(BankAccount.total_accounts)  # Should be 2