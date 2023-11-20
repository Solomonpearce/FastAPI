from fastapi import  FastAPI # para crear la api
from fastapi.responses import HTMLResponse,JSONResponse # para retornar html y contenido en formato Json hacia el cliente
from config.database import engine,Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.users import user_router
'''
uvicorn main:app --reload -- para permitir cambios, ademas con -- port 8000 para cambiar el puerto 
asignado por defecto.
Tambien se puede asignar un host por defectom con, los mismos comandos. Ademas se puede tener un host, para ingresar con
otro dispositivo
Se puede modificar información relevante como versión, nombre , etc .



'''
movies = [
{    'id': 1,
    'title': 'Avengers: Infinity War',
    'overview': 'As the Avengers and their allies have continued to protect the world from threats too large for any one hero to handle, a new danger has emerged from the cosmic shadows: Thanos.',
    'year': 2018,
    'rating': 8.5,
    'category': 'Action | Adventure | Sci-Fi',},
    {    'id': 2,
    'title': 'Avengers: Infinity War',
    'overview': 'As the Avengers and their allies have continued to protect the world from threats too large for any one hero to handle, a new danger has emerged from the cosmic shadows: Thanos.',
    'year': 2018,
    'rating': 8.5,
    'category': 'Action',}


]
app = FastAPI()
app.title = "My First FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler) #para manejar los errores de la api
app.include_router(movie_router) #para incluir las rutas de la api
app.include_router(user_router) #para incluir las rutas de la api

Base.metadata.create_all(bind=engine) #crea la tabla en la base de datos

@app.get("/", tags=["home"]) # tags para agrupar las rutas
def message():
    return HTMLResponse(content="<h1>Hello World</h1>")











