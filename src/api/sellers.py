"""Seller API"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.utils.database import get_db, SellerDB, UserDB
from src.models.seller import SellerCreate, Seller, SellerProfile
from src.api.auth import get_current_user, security

router = APIRouter()

@router.post("/", response_model=Seller)
async def create_seller(seller: SellerCreate, db: Session = Depends(get_db)):
    # Check if user exists
    user = db.query(UserDB).filter(UserDB.id == seller.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.role != "seller":
        raise HTTPException(status_code=400, detail="User must be a seller")

    # Check if seller already exists
    existing = db.query(SellerDB).filter(SellerDB.user_id == seller.user_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Seller profile already exists")

    db_seller = SellerDB(**seller.dict())
    db.add(db_seller)
    db.commit()
    db.refresh(db_seller)
    return db_seller

@router.get("/", response_model=List[Seller])
async def list_sellers(city: str = None, cuisine: str = None, db: Session = Depends(get_db)):
    query = db.query(SellerDB)
    if city:
        query = query.filter(SellerDB.city == city)
    if cuisine:
        query = query.filter(SellerDB.cuisine_type == cuisine)
    return query.all()

@router.get("/{seller_id}", response_model=SellerProfile)
async def get_seller(seller_id: int, db: Session = Depends(get_db)):
    seller = db.query(SellerDB).filter(SellerDB.id == seller_id).first()
    if not seller:
        raise HTTPException(status_code=404, detail="Seller not found")

    return SellerProfile(
        seller=seller,
        menu_items=[],  # TODO: Add menu items
        reviews=[]      # TODO: Add reviews
    )

@router.put("/{seller_id}/verify")
async def verify_seller(seller_id: int, db: Session = Depends(get_db)):
    seller = db.query(SellerDB).filter(SellerDB.id == seller_id).first()
    if not seller:
        raise HTTPException(status_code=404, detail="Seller not found")

    seller.is_verified = True
    db.commit()
    return {"message": "Seller verified successfully"}
