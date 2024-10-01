from fastapi import FastAPI
from app.controller.category_controller import router as category_router

app = FastAPI()

app.include_router(category_router)
