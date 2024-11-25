from sqlalchemy.orm import Session, joinedload
from app.persistance.models.category_models import Category
from app.domain.schemas.category_schema import CategoryCreate

def create_category(db: Session, category: CategoryCreate):
    db_category = Category(name=category.name, parent_id=category.parent_id, description=category.description)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session):
    return db.query(Category).filter(Category.parent_id == None).options(joinedload(Category.subcategories)).all() #db.query(Category).all()

def update_category(db: Session, id_category: int, new_category: CategoryCreate):
    category = db.query(Category).filter(Category.id_category == id_category).first()
    if not category:
        return None
    category.name = new_category.name
    category.parent_id = new_category.parent_id
    db.commit()
    db.refresh(category)
    return category

def delete_category(db: Session, id_category: int):
    category = db.query(Category).filter(Category.id_category == id_category).first()
    if not category:
        return False
    db.delete(category)
    db.commit()
    return True