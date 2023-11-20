from config.database import Base
from sqlalchemy import Column,Integer,String,ForeignKey,Float
class Movie(Base):
    __tablename__='movies'

    id=Column(Integer,primary_key=True)#primary_key=True, es para que sea la llave primaria
    title=Column(String)
    overview=Column(String)
    year=Column(Integer)
    rating=Column(Float)
    category=Column(Integer)