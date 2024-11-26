from sqlalchemy.orm import Session
from app.persistance.repository import chart_data_repository
from app.domain.schemas.chart_data_schema import ChartDataCreate

def create_chart_data(db: Session, chart_data: ChartDataCreate):
  for data_point in chart_data.data_points:
    chart_data_repository.create_chart_data(db, {
      "date": data_point.date,
      "value": data_point.value,
      "category_id": chart_data.category_id,
      "chart_name": chart_data.chart_name,
      "chart_type": chart_data.chart_type,
      "year": chart_data.year
    })

def list_chart_data_by_category(db: Session, category_id: int):
  data_points = chart_data_repository.get_chart_data_by_category(db, category_id)

  charts = {}
  for point in data_points:
    key = (point.chart_name, point.chart_type, point.category_id, point.year)

    if key not in charts:
      charts[key] = {
        "category_id": point.category_id,
        "chart_name": point.chart_name,
        "chart_type": point.chart_type,
        "year": point.year,
        "data_points": []
      }
    
    charts[key]["data_points"].append({
      "id_chart": point.id_chart,
      "date": point.date,
      "value": point.value,
    })

  return list(charts.values())

def delete_chart_by_name(db: Session, chart_name: str):
  deleted_count = chart_data_repository.delete_chart_by_name(db, chart_name)
  return deleted_count > 0 # Devuelve True si eliminó al menos un registro, de lo contrario False

def updated_chart_data_by_name(db: Session, chart_name: str, new_data: ChartDataCreate):
  data_points = [{
    "date": data_point.date,
    "value": data_point.value,
    "category_id": new_data.category_id,
    "chart_name": chart_name,
    "chart_type": new_data.chart_type
  } for data_point in new_data.data_points]

  updated = chart_data_repository.update_chart_data_by_name(db, chart_name, data_points)
  return updated