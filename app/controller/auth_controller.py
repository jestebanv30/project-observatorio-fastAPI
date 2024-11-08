from fastapi import APIRouter, HTTPException, Depends, Response, Request
from sqlalchemy.orm import Session
from app.domain.schemas.users import UserCreate, UserResponse, Token
from app.domain.services.auth_service import create_access_token, create_refresh_token, decode_token
from app.domain.services.user_service import save_user, get_user_by_email, verify_password
from app.config import get_db

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

    # Aquí configuramos el acceso básico a través de cabeceras (sin cookies)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

# Ruta protegida que requiere autenticación
@router.get("/protected-route")
def protected_route(request: Request):
    # Recupera el token del encabezado Authorization
    authorization: str = request.headers.get("Authorization")
    if not authorization:
        raise HTTPException(status_code=403, detail="Not authenticated")

    token = authorization.split(" ")[1]  # Se espera que el token sea pasado como "Bearer <token>"

    try:
        payload = decode_token(token)  # Valida el token
    except Exception as e:
        raise HTTPException(status_code=403, detail=f"Error: {str(e)}")

    return {"message": "This is a protected route", "user": payload}
