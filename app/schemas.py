from pydantic import BaseModel

# Esquema para crear un nuevo ítem
class ItemCreate(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    disponible: bool = True

# Esquema para mostrar un ítem
class Item(BaseModel):
    id: int
    nombre: str
    descripcion: str
    precio: float
    disponible: bool

    class Config:
        orm_mode = True
