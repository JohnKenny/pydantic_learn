from pydantic import BaseModel, Field

class Person(BaseModel):
    name: str = Field(..., min_length=5, max_length=25)
    age: int = Field(default=31, ge=1, le=120)
    zipcode: str = Field(..., pattern=r'^\d{5}$')

person = Person(name="Emma Greene", zipcode="12345")
print(person)
