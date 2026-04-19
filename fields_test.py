from pydantic import BaseModel, Field

class Person(BaseModel):
    name: str = Field()

person = Person("Louise")