# import models as models 
from db import SessionLocal, engine, Base 


def add_tables():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()