"""Pydantic basics - Validators"""

from pydantic import BaseModel, field_validator

class Person(BaseModel):
    name: str
    age: int

juan = Person(name="Juan", age=23)
print(juan)


