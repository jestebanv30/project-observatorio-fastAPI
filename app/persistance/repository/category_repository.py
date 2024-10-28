from sqlalchemy.orm import Session
from app.persistance.models.category_models import Category
from app.domain.schemas.category_schema import CategoryCreate

def create_category(db: Session, category: CategoryCreate):
    db_category = Category(name=category.name, parent_id=category.parent_id)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session):
    return db.query(Category).all()
