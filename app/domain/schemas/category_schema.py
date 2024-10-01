from pydantic import BaseModel

class CategoryCreate(BaseModel):
    name: str

class CategoryResponse(BaseModel):
    id_category: int
    name: str

    class Config:
        orm_mode = True

class FeaturedDataCreate(BaseModel):
    city: str
    percentage: float
    category_id: int

class FeaturedDataResponse(BaseModel):
    id_featured: int
    city: str
    percentage: float

    class Config:
        orm_mode = True