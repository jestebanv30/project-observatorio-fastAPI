from sqlalchemy import Column, Integer, Numeric, ForeignKey, String
from sqlalchemy.orm import relationship
from app.config import Base


class ChartData(Base):
  __tablename__ = "chart_data"

  id_chart = Column(Integer, primary_key=True, index=True)
  date = Column(String, nullable=False)
  value = Column(Numeric, nullable=False)
  category_id = Column(Integer, ForeignKey("categories.id_category"), nullable=False)
  chart_name = Column(String, nullable=False)
  chart_type = Column(String, nullable=False)
  year = Column(Integer, nullable=True)

  category = relationship("Category", backref="chart_data")