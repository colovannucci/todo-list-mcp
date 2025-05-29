from fastapi import FastAPI
from .database import Base, engine
from .routers import lists, items
# Configuración de CORS para permitir solicitudes desde el frontend
from fastapi.middleware.cors import CORSMiddleware


# Crear las tablas en la base de datos si no existen
Base.metadata.create_all(bind=engine)

# Instancia principal de la aplicación FastAPI
app = FastAPI(title="TodoList + MCP (FastAPI)")

# Incluir routers para las rutas de listas e ítems
app.include_router(lists.router)
app.include_router(items.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the TodoList API with MCP (FastAPI)!"}


# Permitir acceso desde frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/hello")
def read_root():
    return {"message": "Hello from FastAPI"}