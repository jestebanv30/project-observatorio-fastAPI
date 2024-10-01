from sqlalchemy import Column, Integer, String
from app.config import Base

class Category(Base):
    __tablename__ = "categories"

    id_category = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
