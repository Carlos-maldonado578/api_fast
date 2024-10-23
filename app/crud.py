from sqlalchemy.orm import Session
from . import models, schemas

# Crear un nuevo ítem
def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.ItemDB(
        nombre=item.nombre,
        descripcion=item.descripcion,
        precio=item.precio,
        disponible=item.disponible
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Obtener todos los ítems
def get_items(db: Session):
    return db.query(models.ItemDB).all()

# Obtener un ítem por ID
def get_item(db: Session, item_id: int):
    return db.query(models.ItemDB).filter(models.ItemDB.id == item_id).first()

# Actualizar un ítem
def update_item(db: Session, item_id: int, item: schemas.ItemCreate):
    db_item = db.query(models.ItemDB).filter(models.ItemDB.id == item_id).first()
    if db_item:
        db_item.nombre = item.nombre
        db_item.descripcion = item.descripcion
        db_item.precio = item.precio
        db_item.disponible = item.disponible
        db.commit()
        db.refresh(db_item)
    return db_item

# Eliminar un ítem por ID
def delete_item(db: Session, item_id: int):
    db_item = db.query(models.ItemDB).filter(models.ItemDB.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
