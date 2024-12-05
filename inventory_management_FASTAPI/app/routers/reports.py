# app/routers/reports.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, models

router = APIRouter()

@router.get("/inventory_levels")
def get_inventory_levels(db: Session = Depends(database.get_db)):
    return db.query(models.Inventory).all()

@router.get("/inventory_movements")
def get_inventory_movements(start_date: str, end_date: str, db: Session = Depends(database.get_db)):
    return db.query(models.Inventory).filter(models.Inventory.date.between(start_date, end_date)).all()

@router.get("/supplier_order_history/{supplier_id}")
def get_supplier_order_history(supplier_id: int, db: Session = Depends(database.get_db)):
    return db.query(models.Inventory).filter(models.Inventory.supplier_id == supplier_id).all()