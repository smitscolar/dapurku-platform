"""Payment API"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from src.utils.database import get_db, PaymentDB
from src.models.payment import PaymentCreate, Payment, PaymentStatus
from src.config import settings

router = APIRouter()

@router.post("/", response_model=Payment)
async def create_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    db_payment = PaymentDB(**payment.dict(), created_at=datetime.utcnow())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

@router.get("/{payment_id}", response_model=Payment)
async def get_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = db.query(PaymentDB).filter(PaymentDB.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@router.post("/{payment_id}/process")
async def process_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = db.query(PaymentDB).filter(PaymentDB.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    # Simulate payment processing
    payment.status = PaymentStatus.COMPLETED
    payment.paid_at = datetime.utcnow()
    payment.transaction_id = f"TRX-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}-{payment.id}"

    db.commit()
    db.refresh(payment)
    return {"message": "Payment processed successfully", "payment": payment}

@router.post("/{payment_id}/refund")
async def refund_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = db.query(PaymentDB).filter(PaymentDB.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    if payment.status != PaymentStatus.COMPLETED:
        raise HTTPException(status_code=400, detail="Payment not completed")

    payment.status = PaymentStatus.REFUNDED
    db.commit()
    return {"message": "Payment refunded successfully"}
