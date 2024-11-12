from pydantic import BaseModel
from typing import List, Optional

class DataPoint(BaseModel):
  id_chart: Optional[int] = None 
  date: str
  value: float

class ChartDataCreate(BaseModel):
  category_id: int
  chart_name: str
  chart_type: str # 'annual' o 'weekly'
  year: Optional[int] = None
  data_points: List[DataPoint]

class ChartDataResponse(BaseModel):
  category_id: int
  chart_name: str
  chart_type: str
  year: Optional[int] = None
  data_points: List[DataPoint]

  class Config:
    orm_mode = True