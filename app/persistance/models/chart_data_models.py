from sqlalchemy import Column, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.config import Base


class ChartData(Base):
  __tablename__ = "chart_data"

  id_chart = Column(Integer, primary_key=True, index=True)
  year = Column(Integer, nullable=False)
  week = Column(Integer, nullable=True) # NULL para datos anuales
  value = Column(Numeric, nullable=False)
  category_id = Column(Integer, ForeignKey("categories.id_category"), nullable=False)

  category = relationship("Category", backref="chart_data")