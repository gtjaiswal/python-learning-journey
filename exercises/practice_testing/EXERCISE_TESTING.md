# Here are Day 5-9 testing challenges - each day builds on the previous one.
**test imports uisng __init__.py**
## Day 5: unittest Basics
    Challenge 5.1: Basic Test Case
    
    You have this Calculator class (provided):
    
    class Calculator:
        def add(self, a, b):
            return a + b
        
        def divide(self, a, b):
            if b == 0:
                raise ValueError("Cannot divide by zero")
            return a / b
        
        def is_even(self, num):
            return num % 2 == 0
    
   
    Write unittest tests:
    1. Test add() with positive numbers
       2. Test add() with negative numbers
       3. Test divide() normal case
       4. Test divide() raises ValueError for zero division
       5. Test is_even() for both even and odd numbers
    
    Use: TestCase, assertEqual, assertRaises, assertTrue, assertFalse
    """
    
    # Your test code here
    Challenge 5.2: setUp and tearDown
    python"""
    You have this FileManager class:
    """
    class FileManager:
        def __init__(self, filename):
            self.filename = filename
            self.file = None
        
        def write(self, content):
            with open(self.filename, 'w') as f:
                f.write(content)
        
        def read(self):
            with open(self.filename, 'r') as f:
                return f.read()
    
    """
    Write tests using setUp and tearDown:
    1. setUp: Create a test file
       2. tearDown: Delete the test file (use os.remove)
       3. Test write() and read() methods
       4. Test that file cleanup happens even if test fails
    
    Hint: Create file in setUp, ensure it's deleted in tearDown
    """
    
    # Your test code here
    Learning goal: Understand test isolation, resource cleanup

## Day 6: pytest Fundamentals
    Challenge 6.1: Simple pytest Functions
    python"""
    Convert Challenge 5.1 (Calculator tests) to pytest style:
    - No class, just test functions
      - Use simple assert statements (no self.assertEqual)
      - Use pytest.raises() for exception testing
      - Run with: pytest -v test_file.py
      """
    
    # Your pytest code here
    Challenge 6.2: Fixtures - Basic
    python"""
    You have this ShoppingCart class:
    """
    class ShoppingCart:
        def __init__(self):
            self.items = []
        
        def add_item(self, item, price):
            self.items.append({"item": item, "price": price})
        
        def get_total(self):
            return sum(item["price"] for item in self.items)
        
        def get_item_count(self):
            return len(self.items)
    
    """
    Write pytest tests using fixtures:
    1. Create a fixture 'empty_cart' that returns a new ShoppingCart
       2. Create a fixture 'cart_with_items' that returns cart with 3 items
       3. Test add_item() using empty_cart
       4. Test get_total() using cart_with_items
       5. Test get_item_count() using both fixtures
    
    Hint: @pytest.fixture decorator
    """
    
    # Your test code here
    Challenge 6.3: conftest.py
    python"""
    Organize your ShoppingCart tests:
    1. Create conftest.py with shared fixtures
       2. Create test_cart_basic.py - test add/remove operations
       3. Create test_cart_calculations.py - test total/count operations
       4. Both test files should use fixtures from conftest.py
    
    Structure:
    tests/
      conftest.py       # Shared fixtures
      test_cart_basic.py
      test_cart_calculations.py
    """
    
    # Your code in 3 separate files
    Learning goal: pytest's discovery, fixture reuse, project structure

## Day 7: pytest Advanced
    Challenge 7.1: Parametrize
    
    You have this PasswordValidator:
    
    class PasswordValidator:
        @staticmethod
        def is_strong(password):
            if len(password) < 8:
                return False
            has_upper = any(c.isupper() for c in password)
            has_lower = any(c.islower() for c in password)
            has_digit = any(c.isdigit() for c in password)
            return has_upper and has_lower and has_digit
    
    """
    Write parametrized tests:
    1. Test multiple valid passwords (should return True)
       2. Test multiple invalid passwords (should return False)
       3. Use @pytest.mark.parametrize to test all cases in one function
       4. Test at least 6 different password scenarios
    
    Example structure:
    @pytest.mark.parametrize("password,expected", [
        # your test cases here
    ])
    """
    
    # Your test code here
    Challenge 7.2: Fixture Scopes
    python"""
    You have this Database class (simulated):
    """
    class Database:
        def __init__(self):
            self.connection_count = 0
            self.data = {}
            print("Database connected")
        
        def connect(self):
            self.connection_count += 1
        
        def insert(self, key, value):
            self.data[key] = value
        
        def get(self, key):
            return self.data.get(key)
        
        def close(self):
            print("Database closed")
    
    """
    Create fixtures with different scopes:
    1. Function-scoped fixture 'db' - new DB for each test
       2. Class-scoped fixture 'shared_db' - one DB for all tests in a class
       3. Module-scoped fixture 'module_db' - one DB for entire module
    
    Write tests that demonstrate:
    - Function scope: each test gets fresh database
      - Class scope: tests share data within a class
      - Module scope: tests share data across the module
    
    Observe connection_count to verify behavior
    """
    
    # Your test code here
    Challenge 7.3: Fixture Dependency & Autouse
    python"""
    Build a test environment for UserService:
    """
    class UserService:
        def __init__(self, db, cache):
            self.db = db
            self.cache = cache
        
        def create_user(self, user_id, name):
            self.db[user_id] = name
            self.cache[user_id] = name
            return True
        
        def get_user(self, user_id):
            # Try cache first, then DB
            if user_id in self.cache:
                return self.cache[user_id]
            return self.db.get(user_id)
    
    """
    Create fixture chain:
    1. Fixture 'db' - returns empty dict
       2. Fixture 'cache' - returns empty dict  
       3. Fixture 'user_service' - depends on db and cache, returns UserService
       4. Autouse fixture 'reset_data' - clears db and cache after each test
    
    Write tests that:
    - Use user_service fixture
      - Verify autouse cleanup works
      - Test cache hit vs DB fallback scenarios
      """
    
    # Your test code here
    Learning goal: Parametrization, fixture scopes, dependency injection

## Day 8: Mocking & Patching
    Challenge 8.1: Basic Mock
    python"""
    You have this EmailService:
    """
    class EmailService:
        def send_email(self, to, subject, body):
            # Actual implementation would send email
            # We don't want to actually send emails in tests!
            import smtplib
            # ... complex SMTP code ...
            return True
    
    class UserRegistration:
        def __init__(self, email_service):
            self.email_service = email_service
        
        def register(self, email, username):
            # ... validation logic ...
            self.email_service.send_email(
                email, 
                "Welcome!", 
                f"Welcome {username}"
            )
            return True
    
    """
    Write tests using unittest.mock:
    1. Create a mock for EmailService
       2. Test UserRegistration.register()
       3. Verify send_email was called with correct arguments
       4. Use mock.assert_called_once_with()
       5. Test registration without actually sending emails
    
    Hint: from unittest.mock import Mock
    """
    
    # Your test code here
    Challenge 8.2: Patching External Dependencies
    python"""
    You have this WeatherService that calls external API:
    """
    import requests
    
    class WeatherService:
        def get_temperature(self, city):
            response = requests.get(f"https://api.weather.com/{city}")
            data = response.json()
            return data['temperature']
        
        def is_hot(self, city):
            temp = self.get_temperature(city)
            return temp > 30
    
    """
    Write tests using patch:
    1. Mock requests.get to avoid actual API calls
       2. Test get_temperature() returns correct value
       3. Test is_hot() for hot and cold temperatures
       4. Use @patch decorator or patch context manager
       5. Verify requests.get was called with correct URL
    
    Hint: from unittest.mock import patch, Mock
    """
    
    # Your test code here
    Challenge 8.3: pytest-mock & MagicMock
    python"""
    You have this PaymentProcessor:
    """
    class PaymentGateway:
        def charge(self, amount, card_number):
            # Would actually charge the card
            pass
        
        def refund(self, transaction_id):
            # Would actually process refund
            pass
    
    class PaymentProcessor:
        def __init__(self, gateway):
            self.gateway = gateway
        
        def process_payment(self, amount, card):
            if amount <= 0:
                raise ValueError("Invalid amount")
            
            result = self.gateway.charge(amount, card)
            return {
                "success": True,
                "transaction_id": result,
                "amount": amount
            }
    
    """
    Write tests using pytest-mock (mocker fixture):
    1. Mock PaymentGateway using mocker.Mock()
       2. Configure mock to return specific transaction_id
       3. Test process_payment() success case
       4. Test that ValueError is raised for invalid amount
       5. Use mocker.patch if needed
       6. Verify gateway.charge was called with correct args
    
    Install: pip install pytest-mock
    """
    
    # Your test code here
    Learning goal: When/what to mock, avoiding real external calls

## Day 9: Testing Best Practices & Integration
    Challenge 9.1: AAA Pattern & Test Organization
    python"""
    You have this OrderService:
    """
    class OrderService:
        def __init__(self, inventory, payment_processor):
            self.inventory = inventory
            self.payment_processor = payment_processor
            self.orders = []
        
        def create_order(self, items, payment_info):
            # Check inventory
            for item in items:
                if not self.inventory.has_stock(item['id'], item['quantity']):
                    return {"success": False, "error": "Out of stock"}
            
            # Calculate total
            total = sum(item['price'] * item['quantity'] for item in items)
            
            # Process payment
            payment_result = self.payment_processor.process(total, payment_info)
            if not payment_result['success']:
                return {"success": False, "error": "Payment failed"}
            
            # Create order
            order_id = len(self.orders) + 1
            self.orders.append({
                "id": order_id,
                "items": items,
                "total": total,
                "status": "confirmed"
            })
            
            # Reduce inventory
            for item in items:
                self.inventory.reduce_stock(item['id'], item['quantity'])
            
            return {"success": True, "order_id": order_id}
    
    """
    Write well-organized tests following AAA pattern:
    1. Test happy path (successful order)
       2. Test out of stock scenario
       3. Test payment failure scenario
       4. Each test should have clear Arrange-Act-Assert sections
       5. Use descriptive test names: test_create_order_success_when_stock_available
       6. Mock both inventory and payment_processor
       7. Add comments marking Arrange, Act, Assert sections
    
    Show good test organization!
    """
    
    # Your test code here
    Challenge 9.2: Testing Edge Cases & Coverage
    python"""
    You have this DiscountCalculator:
    """
    class DiscountCalculator:
        def calculate_discount(self, total, customer_type, coupon_code=None):
            discount = 0
            
            # Customer type discounts
            if customer_type == "premium":
                discount = total * 0.15
            elif customer_type == "regular":
                discount = total * 0.05
            
            # Coupon discounts (additive)
            if coupon_code == "SAVE20":
                discount += total * 0.20
            elif coupon_code == "SAVE10":
                discount += total * 0.10
            
            # Max 50% discount
            if discount > total * 0.5:
                discount = total * 0.5
            
            return total - discount
    
    """
    Write comprehensive tests:
    1. Test all customer types (premium, regular, None/unknown)
       2. Test all coupon codes (SAVE20, SAVE10, invalid, None)
       3. Test combination of customer type + coupon
       4. Test max discount limit (50%)
       5. Test edge case: zero total
       6. Use parametrize for efficiency
       7. Aim for 100% code coverage
    
    Run: pytest --cov=your_module --cov-report=html
    """
    
    # Your test code here
    Challenge 9.3: Integration Test
    python"""
    Build an integration test for this mini-system:
    """
    class Database:
        def __init__(self):
            self.users = {}
        
        def save_user(self, user_id, data):
            self.users[user_id] = data
        
        def get_user(self, user_id):
            return self.users.get(user_id)
    
    class UserValidator:
        @staticmethod
        def validate(email, age):
            if '@' not in email:
                raise ValueError("Invalid email")
            if age < 18:
                raise ValueError("Must be 18+")
    
    class UserService:
        def __init__(self, db, validator):
            self.db = db
            self.validator = validator
        
        def register_user(self, user_id, email, age):
            self.validator.validate(email, age)
            user_data = {"email": email, "age": age, "status": "active"}
            self.db.save_user(user_id, user_data)
            return user_data
        
        def get_user_status(self, user_id):
            user = self.db.get_user(user_id)
            return user['status'] if user else None
    
    """
    Write integration tests:
    1. Test full flow: register user -> retrieve user -> check status
       2. Test validation errors propagate correctly
       3. Use REAL Database and UserValidator (no mocks)
       4. Test multiple users don't interfere with each other
       5. Use fixtures to set up the full system
       6. This tests components working together
    
    Also write unit tests:
    7. Unit test UserService.register_user with mocked dependencies
       8. Compare integration vs unit test approaches
    
    Understand: When to integration test vs unit test
    """
    
    # Your test code here

