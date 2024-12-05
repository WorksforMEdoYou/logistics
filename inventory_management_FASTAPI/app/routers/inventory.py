# app/routers/inventory.py
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, schemas, crud

router = APIRouter()

@router.post("/", response_model=schemas.Inventory)
def create_inventory(inventory: schemas.InventoryCreate, db: Session = Depends(database.get_db)):
    return crud.create_inventory(db=db, inventory=inventory)

@router.get("/{inventory_id}", response_model=schemas.Inventory)
def read_inventory(inventory_id: int, db: Session = Depends(database.get_db)):
    return crud.get_inventory(db=db, inventory_id=inventory_id)

@router.get("/", response_model=List[schemas.Inventory])
def read_inventories(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_inventories(db=db, skip=skip, limit=limit)

@router.put("/{inventory_id}", response_model=schemas.Inventory)
def update_inventory(inventory_id: int, inventory: schemas.InventoryCreate, db: Session = Depends(database.get_db)):
    return crud.update_inventory(db=db, inventory_id=inventory_id, inventory=inventory)

@router.delete("/{inventory_id}", response_model=schemas.Inventory)
def delete_inventory(inventory_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_inventory(db=db, inventory_id=inventory_id)