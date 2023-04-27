from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel 

# http://127.0.0.1:8000/redoc ou doc

class Item(BaseModel):
    nome: str
    descricao: Optional[str] = None
    price: float 
    impostos: Optional[float] = None 

app = FastAPI()

@app.post("/itens/")
async def create_iteam(item: Item):
    return item
