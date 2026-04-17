"""Pydantic basics"""

from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name="Juan", age=32)

print(user)