"""Seller Models"""
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class SellerBase(BaseModel):
    business_name: str
    description: Optional[str] = None
    address: str
    city: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    cuisine_type: Optional[str] = None
    is_verified: bool = False
    rating: float = 0.0
    total_orders: int = 0

class SellerCreate(SellerBase):
    user_id: int

class Seller(SellerBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class SellerProfile(BaseModel):
    seller: Seller
    menu_items: List[dict] = []
    reviews: List[dict] = []
