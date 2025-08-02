"""A file to test the ty type hinting."""

from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field
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
    API_KEY: str = Field(..., description="The API key")
    API_URL: str = Field(..., description="The API URL")

    model_config: ConfigDict = ConfigDict(env_file=".env", env_file_encoding="utf-8")


print(User())
