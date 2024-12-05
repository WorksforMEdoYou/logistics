# app/schemas.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str
    role: Optional[str] = "user"  # Default role

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    description: str
    price: int
    sku: str
    stock_quantity: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True

class SupplierBase(BaseModel):
    name: str
    address: str
    contact_details: str

class SupplierCreate(SupplierBase):
    pass

class Supplier(SupplierBase):
    id: int

    class Config:
        orm_mode = True

class InventoryBase(BaseModel):
    product_id: int
    supplier_id: int
    quantity: int
    transaction_type: str

class InventoryCreate(InventoryBase):
    pass

class Inventory(InventoryBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True