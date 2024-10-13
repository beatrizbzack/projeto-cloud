from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# import db as database  # Importe sua função de conexão com o banco de dados
from .routes import router  # Importe seu roteador onde os endpoints estão definidos

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
DATABASE_URL = "postgresql://cloud:cloud@localhost:5432/2b649a99ee923032cb3d97bedd5c6d950b2b45c876f4607bc87817d019751e5b"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependência para obter a sessão do banco de dados
def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Incluindo os roteadores que contêm os endpoints
app.include_router(router)

# Endpoint inicial (opcional)
@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API!"}


