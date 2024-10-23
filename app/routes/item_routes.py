from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, models, database

router = APIRouter()

# Crear un nuevo ítem
@router.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(database.get_db)):
    return crud.create_item(db=db, item=item)

# Obtener todos los ítems
@router.get("/items/", response_model=list[schemas.Item])
def get_items(db: Session = Depends(database.get_db)):
    return crud.get_items(db)

# Obtener un ítem por ID
@router.get("/items/{item_id}", response_model=schemas.Item)
def get_item(item_id: int, db: Session = Depends(database.get_db)):
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Ítem no encontrado")
    return db_item

# Actualizar un ítem
@router.put("/items/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(database.get_db)):
    db_item = crud.update_item(db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Ítem no encontrado")
    return db_item

# Eliminar un ítem
@router.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(database.get_db)):
    db_item = crud.delete_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Ítem no encontrado")
    return {"message": f"Ítem con id {item_id} eliminado"}
