# app/persistance/repository/category.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.persistance.models.category import Category, FeaturedData
from app.domain.schemas.category import CategoryCreate

async def create_category(db: AsyncSession, category: CategoryCreate):
    new_category = Category(name=category.name)
    db.add(new_category)
    await db.commit()
    await db.refresh(new_category)

    # Agregar los datos destacados asociados
    for data in category.featured_data:
        new_data = FeaturedData(city=data.city, percentage=data.percentage, category_id=new_category.id_category)
        db.add(new_data)
    
    await db.commit()
    return new_category

async def get_category(db: AsyncSession, category_id: int):
    result = await db.execute(select(Category).filter(Category.id_category == category_id))
    return result.scalars().first()

async def get_categories(db: AsyncSession):
    result = await db.execute(select(Category))
    return result.scalars().all()

async def delete_category(db: AsyncSession, category_id: int):
    category = await get_category(db, category_id)
    if category:
        await db.delete(category)
        await db.commit()
        return True
    return False
