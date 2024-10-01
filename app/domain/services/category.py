# app/domain/services/category.py
from app.persistance.repository.category import create_category, get_category, get_categories, delete_category
from app.domain.schemas.category import CategoryCreate
from sqlalchemy.ext.asyncio import AsyncSession

async def create_new_category(db: AsyncSession, category: CategoryCreate):
    # Validación ejemplo: Evitar nombres duplicados (opcional)
    existing_category = await get_category_by_name(db, category.name)
    if existing_category:
        raise ValueError("La categoría ya existe")
    
    return await create_category(db, category)

async def get_category_by_name(db: AsyncSession, name: str):
    categories = await get_categories(db)
    for category in categories:
        if category.name == name:
            return category
    return None

async def delete_existing_category(db: AsyncSession, category_id: int):
    return await delete_category(db, category_id)
