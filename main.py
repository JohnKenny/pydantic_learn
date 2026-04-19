"""Pydantic basics - YAML"""

import yaml 

from pydantic import BaseModel, field_validator, model_validator

class InvalidProdRelease(Exception):
    """Raised when invalid release is found"""


class UserDetails(BaseModel):
    name: str
    role: str

class ReleaseDetails(BaseModel):
    version: str
    deployed_to_production: bool

    @model_validator(mode="after")
    def check_for_valid_release(cls, values):
        for i in {"a", "b", "rc"}:
            if i in values.version and values.deployed_to_production:
                raise InvalidProdRelease("Liberacion de produccion no permitida.")
        return values

class App(BaseModel):
    name: str
    version: float
    user_details: UserDetails
    release_details: ReleaseDetails

    @field_validator("name")
    def check_name(name):
        """Checks for non-empty and no digits"""
        print("Name:")
        if name and name.isalpha():
            return name
        raise ValueError("El nombre es incorrecto")
    


with open("my_config.yaml") as file:
    contents = yaml.safe_load(file.read())["app"]

print(contents, "\n\n")
app = App(**contents)
print(app)


    
