
from pydantic import BaseModel, EmailStr, field_validator, ValidationError, StrictInt

class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

    @field_validator("account_id")
    def validate_account_id(cls,account_id):
        if account_id <= 0:
            raise ValueError("Account id should be greated than zero")
        return account_id

class StrictUser(BaseModel):
    name: str
    email: EmailStr
    account_id: StrictInt  # Use StrictInt to enforce a strict integer

# --- Default Pydantic Behavior (Type Coercion) ---
print("--- Default Coercion ---")
try:
    # Pydantic will convert "123" to an integer automatically.
    user = User(name="jack", email="jack@abc.com", account_id="234234")
    print(f"Coerced user created successfully!")
    print(f"User's account_id: {user.account_id} (type: {type(user.account_id)})")
except ValidationError as e:
    print(f"This won't be printed: {e}")
finally:
    print(user.model_dump_json())
    temp_user = User.model_validate_json(user.model_dump_json())
    print(temp_user)

print("\n" + "-"*20 + "\n")

# --- Strict Mode Behavior ---
print("--- Strict Mode ---")
try:
    # StrictInt will NOT convert the string and will raise an error.
    strict_user = StrictUser(name="jane", email="jane@abc.com", account_id=456)
except ValidationError as e:
    print("Successfully caught expected error in strict mode:")
    print(e)
finally:
    print(strict_user.model_dump())
    print(strict_user.model_dump_json())
