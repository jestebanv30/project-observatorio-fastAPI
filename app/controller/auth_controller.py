import os
from fastapi import APIRouter, HTTPException, Depends, Response, Request
from sqlalchemy.orm import Session
from app.domain.schemas.users import UserCreate, UserResponse, Token
from app.domain.services.auth_service import create_access_token, create_refresh_token, decode_token
from app.domain.services.user_service import save_user, get_user_by_email, verify_password
from app.config import get_db
from datetime import datetime, timedelta, timezone

router = APIRouter()

# Ruta para registrar usuarios
@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = save_user(db, user)
    return UserResponse.from_orm(new_user)

# Ruta para hacer login y obtener el token
@router.post("/login", response_model=Token)
def login(user: UserCreate, response: Response, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    access_token = create_access_token({"sub": db_user.email, "role": db_user.role})
    refresh_token = create_refresh_token({"sub": db_user.email})

    # Detectamos si estamos en un entorno local o producción
    is_local = os.getenv("ENV") == "development"  # Asegúrate de tener esta variable de entorno configurada

    # Configuramos las cookies para almacenar los tokens
    response.set_cookie(
        key="access_token", 
        value=access_token, 
        httponly=True, 
        secure=False,  # Solo en HTTPS si no es local
        samesite="Strict",  # Prevenir CSRF
        expires=datetime.now(timezone.utc) + timedelta(minutes=15)  # Tiempo de expiración con zona horaria UTC
    )
    response.set_cookie(
        key="refresh_token", 
        value=refresh_token, 
        httponly=True, 
        secure=False,  # Solo en HTTPS si no es local
        samesite="Strict",  # Prevenir CSRF
        expires=datetime.now(timezone.utc) + timedelta(days=30)  # Tiempo de expiración con zona horaria UTC
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

# Ruta protegida que requiere autenticación
@router.get("/protected-route")
def protected_route(request: Request):
    # Imprime las cookies para depuración
    print(request.cookies)
    
    access_token = request.cookies.get("access_token")
    if not access_token:
        raise HTTPException(status_code=403, detail="Not authenticated")
    
    # Si el token es un byte string, convertirlo a string
    if isinstance(access_token, bytes):
        access_token = access_token.decode('utf-8')

    try:
        payload = decode_token(access_token)
    except Exception as e:
        raise HTTPException(status_code=403, detail=f"Error: {str(e)}")

    return {"message": "This is a protected route", "user": payload}

# Ruta para hacer logout
@router.post("/logout")
def logout(response: Response):
    # Eliminar las cookies
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    return {"message": "Logged out successfully"}
