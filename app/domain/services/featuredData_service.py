from sqlalchemy.orm import Session
from app.persistance.repository import featuredData_repository
from app.domain.schemas.featuredData_schema import FeaturedDataCreate

def create_featuredData(db: Session, featuredData: FeaturedDataCreate):
    return featuredData_repository.create_featuredData(db, featuredData)

def list_featuredData(db: Session):
    return featuredData_repository.get_featuredData(db)