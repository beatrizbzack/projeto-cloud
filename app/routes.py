from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from .schemas import UserCreate, UserLogin, AuthResponse
from .auth import create_access_token, authenticate_user, get_password_hash, validate_jwt  # Importa a função de validação
from .models import User
from .services import get_db
from .scraping import get_random_fact

router = APIRouter()

# Registrar o usuário
@router.post("/registrar", response_model=AuthResponse)
async def register(user: UserCreate, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=409, detail="Email já registrado")
    
    hashed_password = get_password_hash(user.password)
    new_user = User(name=user.name, email=user.email, hashed_password=hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    # Gera o token de acesso
    token = create_access_token({"sub": new_user.email})

    return {
        "jwt": token,
        "user": {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email
        } 
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
def consultar_data(authorization: str = Header(None)):
    # Verifica se o header Authorization foi enviado corretamente
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=403, detail="JWT ausente ou inválido")

    # Extrai o token do header
    jwt_token = authorization.split(" ")[1]

    # Valida o JWT
    validate_jwt(jwt_token)  # Verifica se o token é válido

    # Faz a chamada para a API de fatos aleatórios
    random_fact = get_random_fact()

    # Retorna o resultado da API de fatos aleatórios
    return random_fact
