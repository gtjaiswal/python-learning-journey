# Implementation Challenge
**test imports uisng __init__.py**

## Dataclass Challenge: Create a BankAccount dataclass with:

    Fields: account_number, balance, account_type
    Validation in __post_init__: balance >= 0
    A method transfer(amount, to_account) that validates and updates both accounts


## Enum Challenge: Create a CardType enum (VISA, MASTERCARD, AMEX) with:

    A method that returns card number validation pattern
    Usage in a validation function


## Context Manager Challenge: Create a context manager that:

    Temporarily changes an account balance
    Restores original balance on exit
    Handles exceptions properly

## Named Tuple - Payment Transaction Parser
    Scenario: You're building a payment processing system that receives transaction data as CSV strings. Use NamedTuple to create immutable transaction records.
    Requirements:
    
    Create a PaymentTransaction NamedTuple with fields:
    
    transaction_id: str
    amount: float
    currency: str
    timestamp: str
    
    
    Add a method is_high_value() that returns True if amount > 10000
    Add a class method from_csv_line(csv_line: str) that parses a CSV string like:
    
       "TXN001,15000.50,USD,2024-12-01T10:30:00"
    
    Add a method to_dict() that converts the transaction to a dictionary
    Create a function parse_transactions(csv_data: str) -> List[PaymentTransaction] that:
    
    Takes multi-line CSV string
    Returns list of PaymentTransaction objects
    Filters out transactions with amount <= 0

    Test Data:
        pythoncsv_data = """TXN001,15000.50,USD,2024-12-01T10:30:00
        TXN002,500.00,EUR,2024-12-01T10:31:00
        TXN003,-100.00,USD,2024-12-01T10:32:00
        TXN004,25000.00,GBP,2024-12-01T10:33:00"""
        
        transactions = parse_transactions(csv_data)
        print(len(transactions))  # Should be 3 (negative filtered out)
        print(transactions[0].is_high_value())  # True
        print(transactions[1].is_high_value())  # False

# Hints:

    For dataclass: Use if self.balance < 0: raise ValueError(...)
    For enum: Store regex patterns as enum values
    For context manager: Use @contextmanager and try/finally
    For NamedTuple : 
        Use cls for class methods: @classmethod def from_csv_line(cls, csv_line: str)
        Split CSV: csv_line.strip().split(',')
        For to_dict(): self._asdict() is built into NamedTuple
        Multi-line split: csv_data.strip().split('\n')
