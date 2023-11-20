import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
sqlite_file_name = 'database.sqlite'
base_dir=os.path.dirname(os.path.realpath(__file__)) #leer directorial actual. 

database_url=f"sqlite:///{os.path.join(base_dir,sqlite_file_name)}"

engine= create_engine(database_url,echo=True)#Motor de la base de datos


Session=sessionmaker(bind=engine) #crea una sesion con la base de datos

Base=declarative_base()#Manejo de la tabla de la base de datos.