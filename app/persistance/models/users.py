from sqlalchemy import Boolean, Column, Integer, String
from app.config import Base  # Asegúrate de que este archivo tenga la configuración correcta de Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)  # Verifica la longitud según el uso esperado
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    role = Column(String(50), default="user")  # Define roles, ej. "admin", "user"
