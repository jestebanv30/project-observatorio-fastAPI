from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.controller.category_controller import router as category_router
from app.controller.featuredData_controller import router as featuredData_router

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(category_router)
app.include_router(featuredData_router)
