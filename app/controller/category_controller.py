from fastapi import APIRouter, Depends, status, HTTPException
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

@router.put("/{id_category}", response_model=CategoryResponse)
def update_category(id_category: int, new_category: CategoryCreate, db: Session = Depends(get_db)):
    category = category_service.update_category(db, id_category, new_category)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Error en actualizar category")
    return category

@router.delete("/{id_category}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(id_category: int, db: Session = Depends(get_db)):
    if not category_service.delete_category(db, id_category):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Error al eliminar category")