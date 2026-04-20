from pydantic import BaseModel

class Vehiculo(BaseModel):
    ruedas: int
    edad: int

class Moto(Vehiculo):
    carreras: bool

class Autobus(Vehiculo):
    pasajeros: int

m = Moto(ruedas=2, edad=3, carreras=True)
print(m, "\n")
a = Autobus(ruedas=4, edad=7, pasajeros=40)
print(a)

class Address(BaseModel):
    street: str
    city: str

class Person(BaseModel):
    name: str
    age: int
    address: Address

p = Person (name="Juan", 
            age=29, 
            address=Address(street="4 main st", city="London"))
print(p)