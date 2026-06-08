"""Buyer API"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from src.utils.database import get_db, BuyerDB
from src.models.buyer import BuyerCreate, Buyer

router = APIRouter()

@router.post("/", response_model=Buyer)
async def create_buyer(buyer: BuyerCreate, db: Session = Depends(get_db)):
    db_buyer = BuyerDB(**buyer.dict(), created_at=datetime.utcnow())
    db.add(db_buyer)
    db.commit()
    db.refresh(db_buyer)
    return db_buyer

@router.get("/", response_model=List[Buyer])
async def list_buyers(db: Session = Depends(get_db)):
    return db.query(BuyerDB).all()

@router.get("/{buyer_id}", response_model=Buyer)
async def get_buyer(buyer_id: int, db: Session = Depends(get_db)):
    buyer = db.query(BuyerDB).filter(BuyerDB.id == buyer_id).first()
    if not buyer:
        raise HTTPException(status_code=404, detail="Buyer not found")
    return buyer

@router.put("/{buyer_id}/favorites/{seller_id}")
async def add_favorite_seller(buyer_id: int, seller_id: int, db: Session = Depends(get_db)):
    buyer = db.query(BuyerDB).filter(BuyerDB.id == buyer_id).first()
    if not buyer:
        raise HTTPException(status_code=404, detail="Buyer not found")

    favorites = buyer.favorite_sellers or []
    if seller_id not in favorites:
        favorites.append(seller_id)
        buyer.favorite_sellers = favorites
        db.commit()

    return {"message": "Seller added to favorites"}
