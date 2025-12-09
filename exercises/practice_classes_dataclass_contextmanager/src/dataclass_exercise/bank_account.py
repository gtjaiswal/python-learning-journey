from dataclasses import dataclass

@dataclass
class BankAccount:
    account_number:int
    balance: float
    account_type : str

    def __post_init__(self):
        if self.balance <0 :
            raise ValueError("Balance cannot be negative")

    def transfer (self, amount:float, to_account:BankAccount)->bool:
        if amount <0 :
            raise ValueError("Transfer amount must be positive")
        else:
            if self.balance < amount:
                raise ValueError ("Insufficient balance for transfer")
            else:
                self.balance -= amount
                to_account.balance += amount
        return True

if __name__=="__main__":
    # Test 1: Creating account with valid balance
    account1 = BankAccount("ACC001", 1000.0, "SAVINGS")
    print(account1)  # Should work fine

    # Test 2: Creating account with negative balance (should fail)
    try:
        account2 = BankAccount("ACC002", -100.0, "CHECKING")
    except ValueError as e:
        print(f"Error caught: {e}")  # Should print your error message

    # Test 3: Successful transfer
    account_a = BankAccount("ACC003", 1000.0, "SAVINGS")
    account_b = BankAccount("ACC004", 500.0, "CHECKING")

    result = account_a.transfer(300.0, account_b)
    print(f"Transfer successful: {result}")  # True
    print(f"Account A balance: {account_a.balance}")  # 700.0
    print(f"Account B balance: {account_b.balance}")  # 800.0

    # Test 4: Transfer more than available (should fail)
    try:
        account_a.transfer(1000.0, account_b)
    except ValueError as e:
        print(f"Error caught: {e}")  # Should print "Insufficient balance..."

    # Test 5: Transfer negative amount (should fail)
    try:
        account_a.transfer(-50.0, account_b)
    except ValueError as e:
        print(f"Error caught: {e}")  # Should print "Transfer amount must be positive"



