from sqlalchemy.orm import Session
from app.persistance.models.chart_data_models import ChartData

def create_chart_data(db: Session, data_point: dict):
  db_chart_data = ChartData(
    year=data_point["year"], 
    week=data_point["week"], 
    value=data_point["value"], 
    category_id=data_point["category_id"])
  db.add(db_chart_data)
  db.commit()
  db.refresh(db_chart_data)
  return db_chart_data

def get_chart_data_by_category(db: Session, category_id: int):
  return db.query(ChartData).filter(ChartData.category_id == category_id).all()