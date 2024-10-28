from pydantic import BaseModel, Field
from typing import Optional, List

class CategoryCreate(BaseModel):
    name: str
    parent_id: Optional[int] = None # Se puede especificar el padre al crear una categoría

class CategoryResponse(BaseModel):
    id_category: int
    name: str
    parent_id: Optional[int] = None # Muestra el id del padre si existe
    subcategories: List["CategoryResponse"] = Field(default_factory=list) # Recursivamente muestra subcategorías

    class Config:
        orm_mode = True

#CategoryResponse.update_forward_refs()