from pydantic import BaseModel, model_validator
from typing import Optional

class User(BaseModel):
    password:str
    confirm_password: str

user = User(password="abc", confirm_password="abc")
