# app/domain/schemas/category.py
from pydantic import BaseModel, Field
from typing import List, Optional

class FeaturedDataCreate(BaseModel):
    city: str = Field(..., example="Valledupar")
    percentage: float = Field(..., example=30.50)

class FeaturedDataResponse(FeaturedDataCreate):
    id_featured: int

    class Config:
        orm_mode = True

class CategoryCreate(BaseModel):
    name: str = Field(..., example="Salud")
    featured_data: List[FeaturedDataCreate] = []

class CategoryResponse(BaseModel):
    id_category: int
    name: str
    featured_data: List[FeaturedDataResponse] = []

    class Config:
        orm_mode = True
