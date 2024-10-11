from fastapi import Depends, HTTPException
from passlib.context import CryptContext
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from datetime import datetime, timedelta
from .models import User
from .db import get_db
from sqlalchemy.orm import Session

SECRET_KEY = "bebequinh4"  # Mude isso para algo seguro
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Função que valida o JWT
def validate_jwt(token: str):
    try:
        # Decodifica o token e verifica a assinatura
        decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded  # Retorna os dados decodificados se o token for válido
    except ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="JWT expirado")
    except InvalidTokenError:
        raise HTTPException(status_code=403, detail="JWT inválido")