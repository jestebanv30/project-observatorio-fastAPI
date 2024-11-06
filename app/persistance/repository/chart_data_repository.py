from sqlalchemy.orm import Session
from app.persistance.models.chart_data_models import ChartData

def create_chart_data(db: Session, data_point: dict):
  db_chart_data = ChartData(
    date=data_point["date"],
    value=data_point["value"],
    category_id=data_point["category_id"],
    chart_name=data_point["chart_name"],
    chart_type=data_point["chart_type"])
  db.add(db_chart_data)
  db.commit()
  db.refresh(db_chart_data)
  return db_chart_data

def get_chart_data_by_category(db: Session, category_id: int):
  return db.query(ChartData).filter(ChartData.category_id == category_id).all()

def delete_chart_by_name(db: Session, chart_name: str):
  deleted_count = db.query(ChartData).filter(ChartData.chart_name == chart_name).delete()
  db.commit()
  return deleted_count # Retorna la cantidad de registros eliminados

def update_chart_data_by_name(db: Session, chart_name: str, new_data: list):
  # Eliminar datos existentes
  db.query(ChartData).filter(ChartData.chart_name == chart_name).delete()
  db.commit()

  # Nuevos datos
  for data_point in new_data:
    create_chart_data(db, data_point)

  return len(new_data) > 0 # Devuelve TRUE si se actualizó
  
  #updated_count = db.query(ChartData).filter(ChartData.chart_name == chart_name).update(new_data)
  #db.commit()
  #return updated_count
