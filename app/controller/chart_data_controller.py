from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.domain.services import chart_data_service
from app.domain.schemas.chart_data_schema import ChartDataCreate, ChartDataResponse
from app.config import get_db

router = APIRouter(prefix="/chart-data", tags=["Chart Data"])
  
@router.post("/", response_model=ChartDataResponse)
def create_chart_data(chart_data: ChartDataCreate, db: Session = Depends(get_db)):
  return chart_data_service.create_chart_data(db, chart_data)

@router.get("/category/{category_id}", response_model=list[ChartDataResponse])
def list_chart_data_by_category(category_id: int, db: Session = Depends(get_db)):
  return chart_data_service.list_chart_data_by_category(db, category_id)