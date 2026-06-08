"""Buyer Models"""
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class BuyerBase(BaseModel):
    user_id: int
    delivery_addresses: List[dict] = []
    favorite_sellers: List[int] = []
    dietary_preferences: List[str] = []
    total_orders: int = 0
    total_spent: float = 0.0

class BuyerCreate(BuyerBase):
    pass

class Buyer(BuyerBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
