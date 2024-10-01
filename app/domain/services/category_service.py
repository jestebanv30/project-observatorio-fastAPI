from sqlalchemy.orm import Session
from app.persistance.repository import category_repository
from app.domain.schemas.category_schema import CategoryCreate

def create_category(db: Session, category: CategoryCreate):
    return category_repository.create_category(db, category)

def list_categories(db: Session):
    return category_repository.get_categories(db)
