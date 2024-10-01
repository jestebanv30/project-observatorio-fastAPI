# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controller import category  # Importar el controlador

app = FastAPI()

# Configurar CORS (opcional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambiar según el dominio que necesites permitir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir las rutas del controlador de categorías
app.include_router(category.router)

# Ruta de prueba para verificar que la aplicación está corriendo
@app.get("/")
def root():
    return {"message": "API is running!"}
