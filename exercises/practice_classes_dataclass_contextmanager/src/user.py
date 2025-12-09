from utils.data_validator import DataValidator
from typing import List

class User:

    user_count : int =0

    @classmethod
    def from_dict(cls, data):
        return User(data["name"], data["email"], data["age"])


    def __init__(self, name:str, email:str, age:int):
        if DataValidator.is_valid_email(email):
            self.email = email
        else:
            raise ValueError("Invalid email")

        if DataValidator.is_positive(age):
            self.age = age
        else:
            raise ValueError("Invalid number")
        self.name = name
        User.user_count+=1

class UserRepository:

    def __init__(self):
        self._users_list: List[User] = []

    def add_user(self, user:User):
        self._users_list.append(user)

    def find_by_email(self, email:str):
        for user in self._users_list:
            if email==user.email:
                return user
        return None



if __name__=="__main__" :
    # Test
    try:
        user_data = {"name": "Alice", "email": "alice@tests.com", "age": 25}
        user1 = User.from_dict(user_data)  # Class method
        user_data = {"name": "User 2", "email": "user2@tests.com", "age": 25}
        user2 = User.from_dict(user_data)  # Class method
        repo1 = UserRepository()
        repo1.add_user(user1)
        repo2 = UserRepository()
        repo2.add_user(user2)
        # repo.add_user(User("Bob", "invalid-email", 30))  # Should raise error
        found_user1 = repo1.find_by_email("alice@tests.com")
        if found_user1:
            print(f"Found user: {found_user1.name}")
    except ValueError as ve:
        print(ve)
    else:
        print(user1.email)
        found_user2 = repo2.find_by_email("alice@tests.com")
        if found_user2:
            print(f"Found user: {found_user2.name}")
