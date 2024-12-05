# app/routers/products.py
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, schemas, crud
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(database.get_db)):
    return crud.create_product(db=db, product=product)

@router.get("/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(database.get_db)):
    return crud.get_product(db=db, product_id=product_id)

@router.get("/", response_model=List[schemas.Product])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_products(db=db, skip=skip, limit=limit)

@router.put("/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(database.get_db)):
    return crud.update_product(db=db, product_id=product_id, product=product)

@router.delete("/{product_id}", response_model=schemas.Product)
def delete_product(product_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_product(db=db, product_id=product_id)