from sqlalchemy import Column, Integer, String, Date, Numeric, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.config import Base

class FeaturedData(Base):
    __tablename__ = "featured_data"

    id_featured = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    date = Column(Date, nullable=False)
    data = Column(Numeric, nullable=False)
    is_main = Column(Boolean, default=False)
    category_id = Column(Integer, ForeignKey('categories.id_category'), nullable=True)
