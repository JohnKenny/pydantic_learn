import json
from pydantic import BaseModel


with open("person.json") as file:
    contents = file.read()
    print(contents)