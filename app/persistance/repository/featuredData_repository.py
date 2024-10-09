from sqlalchemy.orm import  Session
from app.persistance.models.featuredData_models import FeaturedData
from app.domain.schemas.featuredData_schema import FeaturedDataCreate

def create_featuredData(db: Session, featuredData: FeaturedDataCreate):
  db_featuredData = FeaturedData(
    name=featuredData.name, 
    date=featuredData.date, 
    data=featuredData.data, 
    is_main=featuredData.is_main, 
    category_id=featuredData.category_id
    )
  db.add(db_featuredData)
  db.commit()
  db.refresh(db_featuredData)
  return db_featuredData

def get_featuredData(db: Session):
  return db.query(FeaturedData).all()