from pydantic import BaseModel
from typing import List, Optional

class DataPoint(BaseModel):
  year: int
  week: Optional[int] = None # Opcional, solo para datos semanales
  value: float
  
  class Config:
    orm_mode: True

class ChartDataCreate(BaseModel):
  category_id: int
  data_points: List[DataPoint]

class ChartDataResponse(BaseModel):
  id_chart: int
  year: int
  week: Optional[int] = None
  value: float
  category_id: int

  class Config:
    orm_mode = True