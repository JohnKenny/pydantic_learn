"""Pydantic basics"""

from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    age: int
    induction_passed: bool
    #years_service: Optional[int] = 0
    years_service: int | float | str
    awards: list[str | int]



user = User(name="Gemma", age="30", induction_passed=True, years_service="una semana", awards=["lv1", "lv2", 4])

print(user)