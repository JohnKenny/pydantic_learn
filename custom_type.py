from typing import Annotated
from pydantic import BaseModel, AfterValidator

def check_name(name: str) -> str:
    if len(name) < 1 or len(name) > 11:
        raise ValueError("Length incorrect")
    return name

FirstName = Annotated[str, AfterValidator(check_name)]

class Person(BaseModel):
    name: FirstName

a = Person(name="Gemma")
print(a)