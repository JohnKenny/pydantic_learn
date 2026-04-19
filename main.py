"""Pydantic basics - YAML"""

import yaml 

from pydantic import BaseModel, field_validator, model_validator

class App(BaseModel):
    name: str
    version: float

    

with open("my_config.yaml") as file:
    contents = yaml.safe_load(file.read())["app"]

print(contents, "\n\n")
app = App(**contents)
print(app)


    
