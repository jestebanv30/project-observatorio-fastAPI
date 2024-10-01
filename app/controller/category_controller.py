from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.domain.services import category_service
from app.domain.schemas.category_schema import CategoryCreate, CategoryResponse
from app.config import get_db

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/", response_model=CategoryResponse)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return category_service.create_category(db, category)

@router.get("/", response_model=list[CategoryResponse])
def list_categories(db: Session = Depends(get_db)):
    return category_service.list_categories(db)
