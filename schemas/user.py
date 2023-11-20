from pydantic import BaseModel  # para validar los datos que se envian

class User(BaseModel):
    email: str
    password: str

