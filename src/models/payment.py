"""Payment Models"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum

class PaymentStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"

class PaymentMethod(str, Enum):
    MIDTRANS = "midtrans"
    XENDIT = "xendit"
    CASH = "cash"

class PaymentBase(BaseModel):
    order_id: int
    buyer_id: int
    seller_id: int
    amount: float
    payment_method: PaymentMethod = PaymentMethod.MIDTRANS
    status: PaymentStatus = PaymentStatus.PENDING
    transaction_id: Optional[str] = None
    payment_url: Optional[str] = None
    paid_at: Optional[datetime] = None

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
