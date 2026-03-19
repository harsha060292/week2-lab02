from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
    description: Optional[str] = None

fake_db = {}
next_id = 1

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/items", response_model=List[Item])
def list_items():
    return list(fake_db.values())

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = fake_db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items", response_model=Item)
def create_item(item: Item):
    global next_id
    item.id = next_id
    fake_db[next_id] = item
    next_id += 1
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    item.id = item_id
    fake_db[item_id] = item
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del fake_db[item_id]
    return {"detail": "Item deleted"}
