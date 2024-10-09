from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.domain.services import featuredData_service
from app.domain.schemas.featuredData_schema import FeaturedDataCreate, FeaturedDataResponse
from app.config import get_db

router = APIRouter(prefix="/featuredData", tags=["featuredData"])

@router.post("/", response_model=FeaturedDataResponse)
def create_featuredData(category: FeaturedDataCreate, db: Session = Depends(get_db)):
    return featuredData_service.create_featuredData(db, category)

@router.get("/", response_model=list[FeaturedDataResponse])
def list_featuredData(db: Session = Depends(get_db)):
    return featuredData_service.list_featuredData(db)
