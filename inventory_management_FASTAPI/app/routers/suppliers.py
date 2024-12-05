# app/routers/suppliers.py
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, schemas, crud

router = APIRouter()

@router.post("/", response_model=schemas.Supplier)
def create_supplier(supplier: schemas.SupplierCreate, db: Session = Depends(database.get_db)):
    return crud.create_supplier(db=db, supplier=supplier)

@router.get("/{supplier_id}", response_model=schemas.Supplier)
def read_supplier(supplier_id: int, db: Session = Depends(database.get_db)):
    return crud.get_supplier(db=db, supplier_id=supplier_id)

@router.get("/", response_model=List[schemas.Supplier])
def read_suppliers(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_suppliers(db=db, skip=skip, limit=limit)

@router.put("/{supplier_id}", response_model=schemas.Supplier)
def update_supplier(supplier_id: int, supplier: schemas.SupplierCreate, db: Session = Depends(database.get_db)):
    return crud.update_supplier(db=db, supplier_id=supplier_id, supplier=supplier)

@router.delete("/{supplier_id}", response_model=schemas.Supplier)
def delete_supplier(supplier_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_supplier(db=db, supplier_id=supplier_id)