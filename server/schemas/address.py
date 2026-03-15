from pydantic import BaseModel
from uuid import UUID
from typing import Optional


class AddressBase(BaseModel):
    line1: str
    line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None


class AddressCreate(AddressBase):
    merchant_id: UUID


class AddressResponse(AddressBase):
    id: UUID
    merchant_id: UUID

    class Config:
        from_attributes = True