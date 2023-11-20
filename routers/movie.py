from fastapi import APIRouter
from fastapi import Depends,Path,Query # para crear la api
from fastapi.responses import JSONResponse # para retornar html y contenido en formato Json hacia el cliente
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie
movie_router = APIRouter()

@movie_router.get('/movies', tags=["movies"],response_model=list[Movie],dependencies=[Depends(JWTBearer())]) #para validar el token
def get_movies()->list[Movie]:
    db=Session()
    result=MovieService(db).get_movies()
    return JSONResponse(content=jsonable_encoder(result))

@movie_router.get('/movies/{id}', tags=["movies"],response_model=Movie) # para recibir parametros, manejos de parametros de rutas
def get_movie(id: int=Path(ge=1,le=100))->Movie: #validacion de parametros
    db=Session()
    result=MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(content={"message": "Movie not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)



@movie_router.get('/movies/', tags=["movies"],response_model=list[Movie])
def get_movies_category(category: str = Query(min_length=5,max_length=15))->list[Movie]: # El parámetro es opcional
    db=Session()
    result=MovieService(db).get_movies_category(category)
    if not result:
        return JSONResponse(content={"message": "Movie not found"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@movie_router.post('/movies', tags=["movies"],response_model=dict)
def add_movie(movie: Movie)->dict:
    db=Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(content={"message": "Movie added successfully"}, status_code=201)



@movie_router.put('/movies/{id}', tags=["movies"],response_model=dict) #modificar en la API
def update_movie(id:int, movie: Movie)->dict: #recibe el id y los datos a modificar
    db=Session()
    result=db.query(MovieModel).filter(MovieModel.id==id).first()
    if not result:
        return JSONResponse(content={"message": "Movie not found"}, status_code=404)
    MovieService(db).update_movie(id,movie)
    return JSONResponse(content={"message": "Movie updated successfully"}, status_code=200)



@movie_router.delete('/movies/{id}', tags=["movies"],response_model=dict) #eliminacion en la API
def delete_movie(id:int)->dict:
    db=Session()
    result:MovieModel=db.query(MovieModel).filter(MovieModel.id==id).first()
    if not result:
        return JSONResponse(content={"message": "Movie not found"}, status_code=404)
    MovieService(db).delete_movie(id)
    return JSONResponse(content={"message": "Movie deleted successfully"}, status_code=200)

