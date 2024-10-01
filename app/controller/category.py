# app/controller/category.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.domain.schemas.category import CategoryCreate, CategoryResponse
from app.domain.services.category import create_new_category, get_category_by_name, get_categories, delete_existing_category
from app.config.database import get_db

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
async def create_category(category: CategoryCreate, db: AsyncSession = Depends(get_db)):
    try:
        return await create_new_category(db, category)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[CategoryResponse], status_code=status.HTTP_200_OK)
async def list_categories(db: AsyncSession = Depends(get_db)):
    return await get_categories(db)

@router.get("/{category_name}", response_model=CategoryResponse, status_code=status.HTTP_200_OK)
async def get_category(category_name: str, db: AsyncSession = Depends(get_db)):
    category = await get_category_by_name(db, category_name)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(category_id: int, db: AsyncSession = Depends(get_db)):
    success = await delete_existing_category(db, category_id)
    if not success:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"detail": "Category deleted successfully"}
