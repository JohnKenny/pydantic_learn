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

user = User(password="abc", confirm_password="abc")
print(user)


class ItemtoShip(BaseModel):
    name:str
    shipping_needed: bool
    shipping_address: Optional[str] = ""

    @model_validator(mode="after")
    def item_check(self):
        print (vars(self))
        if self.shipping_needed and not self.shipping_address:
            raise ValueError("Direccion de envio no presente.")
        return self

item = ItemtoShip(name="juguete", shipping_needed=True, shipping_address="1 punto principal")
