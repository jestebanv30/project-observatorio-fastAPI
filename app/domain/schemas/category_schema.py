from pydantic import BaseModel, Field
from typing import Optional, List

class CategoryCreate(BaseModel):
    name: str
    parent_id: Optional[int] = None # Se puede especificar el padre al crear una categoría
    description: Optional[str] = None

class CategoryResponse(BaseModel):
    id_category: int
    name: str
    parent_id: Optional[int] = None # Muestra el id del padre si existe
    description: Optional[str] = None
    subcategories: List["CategoryResponse"] = Field(default_factory=list) # Recursivamente muestra subcategorías

    class Config:
        orm_mode = True