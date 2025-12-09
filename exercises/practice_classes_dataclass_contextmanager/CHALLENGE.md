## Challenge 2: Banking System - All Concepts Combined
**test imports uisng __init__.py**
Scenario: Build a mini banking system that demonstrates all concepts working together.
Requirements:
1. Enum - AccountType and TransactionStatus
python# Create AccountType enum with: SAVINGS, CHECKING, BUSINESS
# Each should have a minimum_balance requirement (0, 100, 500)
# Add method: get_interest_rate() that returns (0.03, 0.01, 0.02)

# Create TransactionStatus enum: PENDING, COMPLETED, FAILED, REVERSED
2. NamedTuple - TransactionRecord
python# Create immutable TransactionRecord with:
# - id, amount, status (TransactionStatus), timestamp
# Add method: is_successful() -> bool
3. Dataclass - BankAccount
python# Create BankAccount with:
# - account_number: str
# - account_type: AccountType
# - balance: float = 0.0
# - transaction_history: List[TransactionRecord] = field(default_factory=list)
# - is_active: bool = True

# Validation in __post_init__:
# - balance >= account_type.minimum_balance
# - account_number must be 10 digits

# Methods:
# - deposit(amount: float) -> TransactionRecord
# - withdraw(amount: float) -> TransactionRecord
#   (check minimum balance, return appropriate TransactionRecord)
# - get_completed_transactions() -> List[TransactionRecord]
4. Context Manager - AccountLock
python# Create context manager that:
# - Temporarily deactivates account (is_active = False)
# - Performs operations safely
# - Reactivates account on exit
# - If exception occurs during operation, log it and keep account inactive

# Usage:
# with account_lock(account):
#     # Do maintenance operations
#     account.deposit(1000)
5. Integration - BankingSession
python# Create a context manager class BankingSession that:
# - Takes account_number and connects to account
# - Yields the account object
# - On exit: prints summary (total deposits, withdrawals, final balance)
# - Handles exceptions gracefully
Complete Usage Example:
python# Your code should work like this:

# Create account
account = BankAccount(
    account_number="1234567890",
    account_type=AccountType.CHECKING,
    balance=500.0
)

# Use banking session
with banking_session(account) as acc:
    acc.deposit(1000.0)
    acc.withdraw(200.0)
    acc.deposit(500.0)
# Should print summary on exit

# Perform locked maintenance
with account_lock(account):
    # Maintenance operations
    pass

# Check results
print(f"Final balance: {account.balance}")
print(f"Completed transactions: {len(account.get_completed_transactions())}")
print(f"Interest rate: {account.account_type.get_interest_rate()}")
Hints:
Enum hints:

Store values as tuples: SAVINGS = (0, 0.03) then unpack in properties
Or use @property methods inside enum

Dataclass hints:

Use if not self.account_number.isdigit() or len(self.account_number) != 10:
Create TransactionRecord objects: TransactionRecord(id=..., amount=..., ...)
Use import uuid for generating transaction IDs: str(uuid.uuid4())[:8]

Context manager hints:

For AccountLock, save original state: original_state = account.is_active
For BankingSession, calculate totals by filtering transaction_history
Use exc_type is not None to check if exception occurred

Transaction filtering hint:
python[txn for txn in self.transaction_history if txn.status == TransactionStatus.COMPLETED]

Expected Skills Demonstrated:
✓ NamedTuple for immutable data with methods
✓ Enum with custom values and methods
✓ Dataclass with validation, default factory, and business logic
✓ Class-based context manager (__enter__, __exit__)
✓ Function-based context manager (@contextmanager)
✓ Type hints throughout
✓ Error handling and validation
