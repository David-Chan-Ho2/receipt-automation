from pydantic import BaseModel
from uuid import UUID
from decimal import Decimal
from typing import Optional


class LineItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    quantity: Optional[Decimal] = None
    unit_price: Optional[Decimal] = None
    amount: Decimal

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Kuro Ramen",
                "email": "contact@kuroramen.com",
                "phone": "+1-217-555-1234",
            }
        }
    }


class LineItemCreate(LineItemBase):
    pass


class LineItemResponse(LineItemBase):
    id: UUID

    class Config:
        from_attributes = True
