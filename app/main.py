from fastapi import FastAPI
from .database import engine
from .models import Base
from .routes import item_routes

# Crear las tablas de la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Registrar las rutas
app.include_router(item_routes.router)
