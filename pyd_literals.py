"""Literals""" 
from typing import Literal

from pydantic import BaseModel

regular = Literal["en-stock", "en-prestamo"]
extra = Literal["en-reparacion"]

class Auto(BaseModel):
    status: regular | extra

auto = Auto(status="en-reparacion")
print(auto)