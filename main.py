"""Pydantic basics - Validators"""

from pydantic import BaseModel, field_validator

class Person(BaseModel):
    name: str
    lname: str
    age: int

    # multi-field validator
    @field_validator("name", "lname")
    def check_name_is_alpha(n):
        if not n.isalpha():
            raise ValueError(f"{n} is incorrectly formed.")
        return n.title()
    
    @field_validator("age")
    def check_correct_age(n):
        if n < 1 or n > 120:
            raise ValueError(f"Invalid age field: ... {n}")
        return n


juan = Person(name="juan", lname="gaunt", age=35)
print(juan)

    
