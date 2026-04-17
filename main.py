"""Pydantic basics - Validators"""

from pydantic import BaseModel, field_validator

class Person(BaseModel):
    name: str
    age: int

    @field_validator("name")
    def check_name_is_alpha(n):
        if not n.isalpha():
            raise ValueError
        return n
    
    @field_validator("age")
    def check_correct_age(n):
        if n < 1 or n > 120:
            raise ValueError(f"Invalid age field: ... {n}")
        return n





juan = Person(name="Juan", age=35)
print(juan)

    
