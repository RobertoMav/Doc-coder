"""A file to test the ty type hinting."""

from typing import Annotated

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings


def test_typing(a: int, b: int) -> int:
    return a + b


# print(test_typing(1, 2))

LearningRate = Annotated[float, Field(gt=0, lt=1, description="Learning rate")]


class User(BaseModel):
    learning_rate: LearningRate


# This will fail at runtime (not caught by type checker)
# user: User = User(learning_rate=4.5)

# This works correctly
user: User = User(learning_rate=0.01)
print(f"Learning rate: {user.learning_rate}")

# Let's also test the validation error
try:
    invalid_user = User(learning_rate=4.5)
except Exception as e:
    print(f"Validation error: {e}")


class User(BaseSettings):
    api_key: str
    api_secret: str


# user = User()
# print(user.api_key)
# print(user.api_secret)
# print all the env variables
import os

print(os.environ)
