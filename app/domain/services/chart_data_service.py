from sqlalchemy.orm import Session
from app.persistance.repository import chart_data_repository
from app.domain.schemas.chart_data_schema import ChartDataCreate

def create_chart_data(db: Session, chart_data: ChartDataCreate):
  for data_point in chart_data.data_points:
    chart_data_repository.create_chart_data(db, {
      "year": data_point.year,
      "weak": data_point.week,
      "value": data_point.value,
      "category_id": chart_data.category_id
    })
  return {"message": "Data points agregados correctamente"}

def list_chart_data_by_category(db: Session, category_id: int):
  return chart_data_repository.get_chart_data_by_category(db, category_id)