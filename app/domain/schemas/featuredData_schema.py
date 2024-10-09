from pydantic import BaseModel
from datetime import date
from typing import Optional

class FeaturedDataCreate(BaseModel):
    name: str
    date: date
    data: float
    is_main: bool
    category_id: Optional[int]

class FeaturedDataResponse(BaseModel):
    id_featured: int
    name: str
    data: float
    date: date
    is_main: bool
    category_id: Optional[int]

    class Config:
        orm_mode = True
