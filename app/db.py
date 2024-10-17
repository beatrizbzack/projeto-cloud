from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 

# colocar senha e user no venv
DATABASE_URL = "postgresql://cloud:cloud@db/database"

engine = create_engine(DATABASE_URL)

# Cria sessão para o db 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


