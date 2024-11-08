# app/services/user_service.py
from sqlalchemy.orm import Session
from app.persistance.models.users import User
from app.persistance.repository import user_repository
from app.domain.schemas.users import UserCreate

def save_user(db: Session, user: UserCreate):
    return user_repository.create_user(db, user)

def get_user_by_email(db: Session, email: str):
    return user_repository.get_user_by_email(db, email)

def get_password_hash(password: str):
    return user_repository.get_password_hash(password)

def verify_password(plain_password, hashed_password):
    return user_repository.verify_password(plain_password, hashed_password)
