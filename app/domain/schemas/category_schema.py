from pydantic import BaseModel

class CategoryCreate(BaseModel):
    name: str

class CategoryResponse(BaseModel):
    id_category: int
    name: str

    class Config:
        orm_mode = True
