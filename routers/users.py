from fastapi import APIRouter
from utils.jwt_manager import create_token
from fastapi.responses import JSONResponse # para retornar html y contenido en formato Json hacia el cliente
from schemas.user import User
user_router=APIRouter()

    
@user_router.post("/login", tags=["auth"])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password=="admin":
        token:str=create_token(user.dict()) #se crea el token con los datos del usuario
        return JSONResponse(status_code=200, content=token)#retorna el usuario que se envia

