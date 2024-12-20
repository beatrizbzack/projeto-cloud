from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from .schemas import UserCreate, UserLogin, AuthResponse
from .auth import create_access_token, authenticate_user, get_password_hash, validate_jwt  # Importa a função de validação
from .models import User
from .services import get_db
from .scraping import get_random_fact
from fastapi.security import OAuth2PasswordBearer 
from typing import Annotated 
from fastapi import Request

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Registrar o usuário
@router.post("/registrar", response_model=dict)
async def register(user: UserCreate, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=409, detail="Email já registrado")
    

    hashed_password = get_password_hash(user.password)
    new_user = User(name=user.name, email=user.email, hashed_password=hashed_password)

    # Gera o token de acesso
    # print(type(new_user.email))
    token = create_access_token({"sub": new_user.email})

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    

    return {
        "jwt": token
    } 

# Faça login 
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = create_access_token({"sub": db_user.email})
    return {"jwt": token}



# Endpoint GET /consultar que exige autenticação via JWT
@router.get("/consultar")
def consultar_data(token: Annotated[str, Depends(oauth2_scheme)]):
    # O token já é passado diretamente, não precisa de verificação extra.
    try:
        # Valida o JWT
        decoded_token = validate_jwt(token)
    except HTTPException as e:
        # Lida com exceções de validação
        raise e

    # Faz a chamada para a API de fatos aleatórios
    random_fact = get_random_fact()

    # Retorna o resultado da API de fatos aleatórios
    return random_fact
