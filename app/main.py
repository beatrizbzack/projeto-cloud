from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .db import Base, engine  # Importa o Base para criação das tabelas
from .routes import router  # Importe seu roteador onde os endpoints estão definidos
import os 
 
# Criação da instância FastAPI
app = FastAPI()

# Configuração do CORS (Cross-Origin Resource Sharing) se necessário
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Altere conforme suas necessidades de segurança
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializa o banco de dados
DATABASE_URL = os.getenv("DATABASE_URL")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependência para obter a sessão do banco de dados
def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Criar as tabelas do banco de dados
@app.on_event("startup")
def startup():
    print("Criando tabelas no banco de dados...")
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso!")


# Incluindo os roteadores que contêm os endpoints
app.include_router(router)

# Endpoint inicial (opcional)
@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API!"}


