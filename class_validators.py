from pydantic import BaseModel, model_validator
from typing import Optional

class User(BaseModel):
    password:str
    confirm_password: str

    @model_validator(mode="after")
    def password_check(self):
        print(vars(self))
        if self.password != self.confirm_password:
            raise ValueError("No coincide.")
        return self

user = User(password="abc", confirm_password="abcd")
print(user)