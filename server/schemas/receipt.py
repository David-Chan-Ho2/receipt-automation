from pydantic import BaseModel
from uuid import UUID
from decimal import Decimal
from datetime import datetime
from typing import Optional, List

from schemas.line_item import LineItemResponse, LineItemCreate


class ReceiptBase(BaseModel):
    currency: str = "USD"
    subtotal: Optional[Decimal] = None
    tax: Optional[Decimal] = None
    tip: Optional[Decimal] = None
    total: Decimal
    payment_method: Optional[str] = None
    purchased_at: Optional[datetime] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "merchant_id": "f6a84f6c-4c25-4c18-bd18-7e89db0a54c1",
                "address_id": "c4f33b75-7e3a-4a41-97f4-3b04e7b7bb62",
                "currency": "USD",
                "subtotal": 56.95,
                "tax": 12.71,
                "tip": 6.70,
                "total": 76.36,
                "payment_method": "VISA CREDIT",
                "purchased_at": "2024-09-28T12:44:00Z",
            }
        }
    }


class ReceiptCreate(ReceiptBase):
    merchant_id: UUID
    address_id: Optional[UUID] = None
    items: List[LineItemCreate]


class ReceiptResponse(ReceiptBase):
    id: UUID
    merchant_id: UUID
    address_id: Optional[UUID]
    items: List[LineItemResponse]

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "example": {
                "id": "bb8f06c1-5c23-4e36-9f1e-2e7b0d87fbb7",
                "merchant_id": "f6a84f6c-4c25-4c18-bd18-7e89db0a54c1",
                "address_id": "c4f33b75-7e3a-4a41-97f4-3b04e7b7bb62",
                "currency": "USD",
                "subtotal": 56.95,
                "tax": 12.71,
                "tip": 6.70,
                "total": 76.36,
                "payment_method": "VISA CREDIT",
                "purchased_at": "2024-09-28T12:44:00Z",
                "items": [
                    {
                        "name": "House Salad",
                        "quantity": 1,
                        "unit_price": 7.95,
                        "amount": 7.95,
                    },
                    {
                        "name": "Kuro Ramen",
                        "quantity": 1,
                        "unit_price": 15.00,
                        "amount": 15.00,
                    },
                    {
                        "name": "Chicken Katsu Curry",
                        "quantity": 1,
                        "unit_price": 16.00,
                        "amount": 16.00,
                    },
                ],
            }
        },
    }