from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "message": "API em execução com sucesso!"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "environment": "production_ready"}

def test_create_item():
    payload = {"name": "Servidor AWS", "price": 49.99, "in_stock": True}
    response = client.post("/items/", json=payload)
    assert response.status_code == 200
    assert response.json()["item"]["name"] == "Servidor AWS"