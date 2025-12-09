"""
This script demonstrates how to correctly import and use the BankAccount class
from the 'src' package.
"""

# Import the BankAccount class from the 'src' package.
# This works because __init__.py "promotes" BankAccount to the top level.
from src import BankAccount


def main():
    """Main function to tests the BankAccount class."""
    print("--- Testing BankAccount from package ---")
    acc = BankAccount(account_number="123-456", balance=1000)
    print(f"Created account: {acc.account_number} with balance: ${acc.get_balance():.2f}")
    print(f"Bank: {acc.bank_name}")


if __name__ == "__main__":
    main()