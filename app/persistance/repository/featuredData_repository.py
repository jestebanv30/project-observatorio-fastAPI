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

def get_featuredData_by_categoryId(db: Session, category_id: int):
    return db.query(FeaturedData).filter(FeaturedData.category_id == category_id).all()

def update_featuredData(db: Session, id_featured: int, new_featuredData: FeaturedDataCreate):
    featured = db.query(FeaturedData).filter(FeaturedData.id_featured == id_featured).first()
    if not featured:
        return None
    featured.name = new_featuredData.name
    featured.data = new_featuredData.data
    featured.date = new_featuredData.date
    featured.is_main = new_featuredData.is_main
    featured.category_id = new_featuredData.category_id
    db.commit()
    db.refresh(featured)
    return featured

def delete_featuredData(db: Session, id_featured: int):
    featured = db.query(FeaturedData).filter(FeaturedData.id_featured == id_featured).first()
    if not featured:
        return False
    db.delete(featured)
    db.commit()
    return True