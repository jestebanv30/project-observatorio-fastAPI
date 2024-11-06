from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.domain.services import chart_data_service
from app.domain.schemas.chart_data_schema import ChartDataCreate, ChartDataResponse
from app.config import get_db

router = APIRouter(prefix="/chart-data", tags=["Chart Data"])

# Ruta para crear datos de gráfica
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_chart_data(chart_data: ChartDataCreate, db: Session = Depends(get_db)):
  try:
    chart_data_service.create_chart_data(db, chart_data)
    return {"message": "Se creó los datos de gráficos correctamente"}
  except Exception:
    raise HTTPException(status_code=500, detail="Error al guardar los datos")

# Ruta para listar gráficas por categoría
@router.get("/category/{category_id}", response_model=list[ChartDataResponse])
def list_chart_data_by_category(category_id: int, db: Session = Depends(get_db)):
  data_points = chart_data_service.list_chart_data_by_category(db, category_id)
  if not data_points:
    raise HTTPException(status_code=404, detail="No se encontraron datos para la categoría solicitada")
  return data_points

# Ruta para eliminar gráfico completo (por nombre, porque se agrupan los datos por nombre del gráfico)
@router.delete("/", status_code=status.HTTP_200_OK)
def delete_chart_by_name(chart_name: str, db: Session = Depends(get_db)):
  deleted = chart_data_service.delete_chart_by_name(db, chart_name)
  if not deleted:
    raise HTTPException(status_code=404, detail=f"El gráfico '{chart_name}' no se encontró")
  return {"message": f"La gráfica con nombre '{chart_name}' se eliminó correctamente"}

@router.put("/{chart_name}", status_code=status.HTTP_200_OK)
def updated_chart_data_by_name(chart_name: str, new_data: ChartDataCreate, db: Session = Depends(get_db)):
  updated = chart_data_service.updated_chart_data_by_name(db, chart_name, new_data)
  if not updated:
    raise HTTPException(status_code=404, detail=f"No se encontró la gráfica con nombre '{chart_name}' para actualizar")
  return {"message": f"La gráfica con nombre '{chart_name}' se actualizó correctamente"}