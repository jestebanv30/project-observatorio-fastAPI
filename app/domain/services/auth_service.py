from datetime import datetime, timedelta, timezone
from authlib.jose import JsonWebToken, JoseError
from app.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_DAYS
from fastapi import HTTPException, status

# Inicializa el objeto JsonWebToken con el algoritmo
jwt = JsonWebToken([ALGORITHM])

def create_token(data: dict, expires_delta: timedelta):
    expire = datetime.now(timezone.utc) + expires_delta  # Calcula el tiempo de expiración
    data.update({"exp": expire})  # Añade la fecha de expiración al payload
    header = {"alg": ALGORITHM}
    return jwt.encode(header, data, SECRET_KEY).decode("utf-8")  # Genera y devuelve el token como cadena

def create_access_token(data: dict):
    return create_token(data, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))

def create_refresh_token(data: dict):
    return create_token(data, timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS))

def decode_token(token: str):
    try:
        # Decodifica y valida el token automáticamente
        claims = jwt.decode(token, SECRET_KEY)
        claims.validate()  # Validar el reclamo, incluyendo expiración
        return claims
    except JoseError as e:
        # El mensaje de error puede ser ajustado según el caso
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired or invalid",
        )
