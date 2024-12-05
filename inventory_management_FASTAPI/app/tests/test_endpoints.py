# app/tests/test_endpoints.py
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal

client = TestClient(app)

@pytest.fixture
def db():
    db = SessionLocal()
    yield db
    db.close()

def test_create_product(db):
    response = client.post("/products/", json={"name": "Test Product", "description": "Test Description", "price": 100, "sku": "TP001", "stock_quantity": 50})
    assert response.status_code == 201
    assert response.json()["name"] == "Test Product"

def test_read_product(db):
    response = client.get("/products/1")
    assert response.status_code == 200

def test_update_product(db):
    response = client.put("/products/1", json={"name": "Updated Product", "description": "Updated Description", "price": 150, "sku": "TP001", "stock_quantity": 75})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Product"

def test_delete_product(db):
    response = client.delete("/products/1")
    assert response.status_code == 200
