from sqlalchemy.orm import Session
from app.persistance.repository import featuredData_repository
from app.domain.schemas.featuredData_schema import FeaturedDataCreate

def create_featuredData(db: Session, featuredData: FeaturedDataCreate):
    return featuredData_repository.create_featuredData(db, featuredData)

def list_featuredData(db: Session):
    return featuredData_repository.get_featuredData(db)

def list_featuredData_by_categoryId(db: Session, category_id: int):
    return featuredData_repository.get_featuredData_by_categoryId(db, category_id)

def update_featuredData(db: Session, id_featured: int, new_featuredData: FeaturedDataCreate):
    return featuredData_repository.update_featuredData(db, id_featured, new_featuredData)

def delete_featuredData(db: Session, id_featured: int):
    return featuredData_repository.delete_featuredData(db, id_featured)