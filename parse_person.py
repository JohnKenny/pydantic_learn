import json
from pydantic import BaseModel

class Person(BaseModel):
    name:str
    location: str
    age: int

    @classmethod
    def make_person_from_json(cls, file_path: str) -> Person:
        with open(file_path) as file:
            return cls(**json.loads(file.read()))
        
person = Person.make_person_from_json("person.json")
print(person)

# with open("person.json") as file:
#     contents = json.loads(file.read())
#     person = Person(**contents)
#     print(person)