from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config import Base

class Category(Base):
    __tablename__ = "categories"

    id_category = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)
    parent_id = Column(Integer, ForeignKey("categories.id_category"), nullable=True)
    description = Column(String, nullable=True)

    parent = relationship("Category", remote_side=[id_category], backref="subcategories")