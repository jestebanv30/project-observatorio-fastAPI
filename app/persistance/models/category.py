# app/persistance/models/category.py
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.config.database import Base

class Category(Base):
    __tablename__ = 'categories'

    id_category = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    
    # Relación uno a muchos
    featured_data = relationship("FeaturedData", back_populates="category", cascade="all, delete-orphan")

class FeaturedData(Base):
    __tablename__ = 'featured_data'

    id_featured = Column(Integer, primary_key=True, index=True)
    city = Column(String(100), nullable=False)
    percentage = Column(Float, nullable=False)
    
    category_id = Column(Integer, ForeignKey('categories.id_category'), nullable=False)
    
    # Relación inversa
    category = relationship("Category", back_populates="featured_data")
