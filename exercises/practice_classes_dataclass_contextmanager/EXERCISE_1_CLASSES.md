# Here are 5 exercises that will reveal your gaps. Try them in order - they progressively test different aspects.
**test imports uisng __init__.py**
## Exercise 1: Basic Class with Methods
    Goal: Test instance/class variables, basic methods
    
    Create a BankAccount class:
        - Initialize with account_number and balance (default 0)
        - Add a class variable 'bank_name' = "Python Bank"
        - Add a class variable 'total_accounts' that increments with each new account
        - Methods: deposit(amount), withdraw(amount), get_balance()
        - withdraw() should return False if insufficient funds, True if success
      
    
    # Your code here
    
    # Test it:
        acc1 = BankAccount("ACC001", 1000)
        acc2 = BankAccount("ACC002")
        print(acc1.deposit(500))  # Should work
        print(acc1.withdraw(2000))  # Should return False
        print(BankAccount.total_accounts)  # Should be 2

## Exercise 2: Magic Methods
    Goal: Test understanding of __str__, __repr__, __eq__, etc.
   
    Create a Book class:
        - Attributes: title, author, isbn, year
        - Implement __str__() to return: "Title by Author (Year)"
        - Implement __repr__() to return: "Book('Title', 'Author', 'ISBN', Year)"
        - Implement __eq__() to compare books by isbn only
        - Implement __lt__() to compare books by year (for sorting)
    
    
    # Your code here
    
    # Test it:
        book1 = Book("1984", "Orwell", "123", 1949)
        book2 = Book("1984", "Orwell", "123", 1949)
        print(book1)  # Should use __str__
        print(repr(book1))  # Should use __repr__
        print(book1 == book2)  # Should be True (same isbn)
        books = [book1, Book("Dune", "Herbert", "456", 1965)]
        print(sorted(books))  # Should sort by year

## Exercise 3: Properties & Validation
    Goal: Test @property, setters, validation logic
    
    Create an Employee class:
        - Private attribute _salary (use single underscore convention)
        - Property 'salary' with getter and setter
        - Setter should validate: salary must be positive, max 1000000
        - Property 'annual_bonus' (read-only) returns 10% of salary
        - Raise ValueError with descriptive message for invalid salary

    
    # Your code here
    
    # Test it:
        emp = Employee("John", 50000)
        print(emp.salary)  # 50000
        print(emp.annual_bonus)  # 5000
        emp.salary = 60000  # Should work
        # emp.salary = -1000  # Should raise ValueError
        # emp.annual_bonus = 10000  # Should raise AttributeError (read-only)

## Exercise 4: Inheritance & super()
    Goal: Test inheritance, method overriding, super()
    
    Create a class hierarchy:
    
    1. Vehicle (base class):
       - Attributes: brand, model, year
       - Method: get_info() returns "Year Brand Model"
       
       2. Car (inherits Vehicle):
          - Additional attribute: num_doors
          - Override get_info() to include doors: "Year Brand Model (Doors doors)"
          - Use super() to call parent's get_info()
       
       3. ElectricCar (inherits Car):
          - Additional attribute: battery_capacity
          - Override get_info() to include battery
          - Use super() properly
    
    
    # Your code here
    
    # Test it:
        vehicle = Vehicle("Toyota", "Generic", 2020)
        car = Car("Honda", "Civic", 2021, 4)
        ev = ElectricCar("Tesla", "Model 3", 2023, 4, 75)
        print(vehicle.get_info())
        print(car.get_info())
        print(ev.get_info())

## Exercise 5: Class Methods, Static Methods & Composition
    Goal: Test @classmethod, @staticmethod, when to use composition
    
    Create a data processing system:
    
        1. DataValidator class (utility class):
           - Static method: is_valid_email(email) - checks if '@' and '.' present
           - Static method: is_positive(number) - checks if number > 0
       
       2. User class:
          - Attributes: name, email, age
          - Use DataValidator in __init__ to validate email and age
          - Class method: from_dict(data) - creates User from dictionary
          - Class variable: user_count
       
       3. UserRepository class (composition):
          - Has a list of User objects
          - Methods: add_user(user), find_by_email(email), get_all_adults()
          - Don't inherit from User - use composition!
      
    
    # Your code here
    
    # Test it:
        user_data = {"name": "Alice", "email": "alice@test.com", "age": 25}
        user1 = User.from_dict(user_data)  # Class method
        repo = UserRepository()
        repo.add_user(user1)
        # repo.add_user(User("Bob", "invalid-email", 30))  # Should raise error
        print(repo.find_by_email("alice@test.com"))
