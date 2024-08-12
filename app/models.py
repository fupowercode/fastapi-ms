# app/models.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Product(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    created_at: datetime
    category: Optional[str]
