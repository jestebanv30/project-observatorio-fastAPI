from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.domain.services import featuredData_service
from app.domain.schemas.featuredData_schema import FeaturedDataCreate, FeaturedDataResponse
from app.config import get_db

router = APIRouter(prefix="/featuredData", tags=["featuredData"])

@router.post("/", response_model=FeaturedDataResponse)
def create_featuredData(featuredData: FeaturedDataCreate, db: Session = Depends(get_db)):
    return featuredData_service.create_featuredData(db, featuredData)

@router.get("/", response_model=list[FeaturedDataResponse])
def list_featuredData(db: Session = Depends(get_db)):
    return featuredData_service.list_featuredData(db)

@router.get("/category/{category_id}", response_model=list[FeaturedDataResponse])
def get_featuredData_by_categoryId(category_id: int, db: Session = Depends(get_db)):
    return featuredData_service.list_featuredData_by_categoryId(db, category_id)

@router.put("/{id_featured}", response_model=FeaturedDataResponse)
def update_featuredData(id_featured: int, new_featuredData: FeaturedDataCreate, db: Session = Depends(get_db)):
    featured = featuredData_service.update_featuredData(db, id_featured, new_featuredData)
    if not featured:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Error en actualizar FeatuedData")
    return featured

@router.delete("/{id_featured}", status_code=status.HTTP_204_NO_CONTENT)
def delete_featuredData(id_featured: int, db: Session = Depends(get_db)):
    if not featuredData_service.delete_featuredData(db, id_featured):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Error al eliminar FeaturedData")