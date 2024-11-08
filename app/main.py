from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controller import file_controller, category_controller, featuredData_controller, auth_controller

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(category_controller.router)
app.include_router(featuredData_controller.router)
app.include_router(file_controller.router)
app.include_router(auth_controller.router, prefix="/auth")

