from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Cloud-Native REST API",
    description="API para esteira de DevSecOps e deploy na AWS",
    version="1.0.0"
)

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.get("/")
def read_root():
    return {"status": "healthy", "message": "API em execução com sucesso!"}

@app.get("/health")
def health_check():
    return {"status": "ok", "environment": "production_ready"}

@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item criado com sucesso", "item": item}