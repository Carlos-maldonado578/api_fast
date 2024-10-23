# FastAPI Project - CRUD con SQLite

Este proyecto es una API RESTful construida con **FastAPI** y **SQLAlchemy**, que utiliza una base de datos **SQLite** para manejar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) de ítems.

## Requisitos previos

Asegúrate de tener instalados los siguientes componentes antes de ejecutar el proyecto:

- **Python 3.7 o superior**
- **pip** (el gestor de paquetes de Python)
- **jq** (una utilidad para manipular datos JSON `OPCIONAL`, ya que se pueden pasar los datos de a uno para poblar la base)

### Instalación de **jq**:
- **Windows**:
  - Usar **winget**: `winget install jqlang.jq`
  - Usar **scoop**: `scoop install jq`
  - Usar **Chocolatey**: `choco install jq`
- **Linux/macOS**:
  - Usar **apt** (Debian/Ubuntu): `sudo apt-get install jq`
  - Usar **brew** (macOS): `brew install jq`

## Instrucciones para levantar el proyecto

### 1. Clonar el repositorio

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/usuario/mi-repositorio.git
cd mi-repositorio
```

### 2. Crear el ambiente virtual

En Linux/macOS:
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```

En Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```
En Windows con git Bash:
```bash
python -m venv venv
source venv/Scripts/activate
```

### 3. Instala las dependencias necesarias listadas en el archivo requirements.txt
```bash
pip install -r requirements.txt
```
Una vez instaladas las dependencias, puedes levantar el servidor usando Uvicorn:
```bash
uvicorn app.main:app --reload
```

Asegúrate de que el archivo populate_db.sh sea ejecutable:
```bash
chmod +x populate_db.sh
```

Luego, puedes ejecutar el script:
```bash
./populate_db.sh
```

El servidor estará corriendo en http://127.0.0.1:8000

### 4. Acceder a la documentación de la API

FastAPI genera documentación automática basada en OpenAPI. Puedes acceder a la interfaz gráfica de la documentación en:

Swagger UI: http://127.0.0.1:8000/docs
