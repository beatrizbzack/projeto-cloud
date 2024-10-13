from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 

DATABASE_URL = "postgresql://cloud:cloud@localhost/database"

engine = create_engine(DATABASE_URL)

# Cria sessão para o db 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


