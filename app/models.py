from sqlalchemy import Column, Integer, String, Float, Boolean
from .database import Base

class ItemDB(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    descripcion = Column(String, index=True)
    precio = Column(Float)
    disponible = Column(Boolean, default=True)
