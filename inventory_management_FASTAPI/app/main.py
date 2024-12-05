# app/main.py
from fastapi import FastAPI
from .database import engine, Base
from .routers import products, suppliers, inventory, reports
from .auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(suppliers.router, prefix="/suppliers", tags=["suppliers"])
app.include_router(inventory.router, prefix="/inventory", tags=["inventory"])
app.include_router(reports.router, prefix="/reports", tags=["reports"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])