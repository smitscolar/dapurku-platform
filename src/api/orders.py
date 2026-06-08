"""Order API"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from src.utils.database import get_db, OrderDB
from src.models.order import OrderCreate, Order, OrderUpdate, OrderStatus
from src.api.auth import get_current_user, security

router = APIRouter()

@router.post("/", response_model=Order)
async def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    # Calculate totals
    total = sum(item.subtotal for item in order.items)
    commission = total * 0.12  # 12% commission

    db_order = OrderDB(
        buyer_id=order.buyer_id,
        seller_id=order.seller_id,
        items=[item.dict() for item in order.items],
        delivery_address=order.delivery_address,
        delivery_lat=order.delivery_lat,
        delivery_lng=order.delivery_lng,
        delivery_fee=order.delivery_fee,
        commission=commission,
        total=total + order.delivery_fee,
        status=OrderStatus.PENDING,
        notes=order.notes,
        created_at=datetime.utcnow()
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@router.get("/", response_model=List[Order])
async def list_orders(
    buyer_id: int = None,
    seller_id: int = None,
    status: OrderStatus = None,
    db: Session = Depends(get_db)
):
    query = db.query(OrderDB)
    if buyer_id:
        query = query.filter(OrderDB.buyer_id == buyer_id)
    if seller_id:
        query = query.filter(OrderDB.seller_id == seller_id)
    if status:
        query = query.filter(OrderDB.status == status)
    return query.order_by(OrderDB.created_at.desc()).all()

@router.get("/{order_id}", response_model=Order)
async def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(OrderDB).filter(OrderDB.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.put("/{order_id}", response_model=Order)
async def update_order(order_id: int, update: OrderUpdate, db: Session = Depends(get_db)):
    order = db.query(OrderDB).filter(OrderDB.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    if update.status:
        order.status = update.status
    if update.notes:
        order.notes = update.notes
    order.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(order)
    return order

@router.get("/seller/{seller_id}/stats")
async def get_seller_order_stats(seller_id: int, db: Session = Depends(get_db)):
    orders = db.query(OrderDB).filter(OrderDB.seller_id == seller_id).all()
    total_orders = len(orders)
    total_revenue = sum(o.total - o.commission for o in orders)
    total_commission = sum(o.commission for o in orders)

    return {
        "seller_id": seller_id,
        "total_orders": total_orders,
        "total_revenue": total_revenue,
        "total_commission": total_commission,
        "avg_order_value": total_revenue / total_orders if total_orders > 0 else 0
    }
