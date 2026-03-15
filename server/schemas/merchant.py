from pydantic import BaseModel, EmailStr
from uuid import UUID
from typing import Optional


class MerchantBase(BaseModel):
    name: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Kuro Ramen",
                "email": "contact@kuroramen.com",
                "phone": "+1-217-555-1234",
            }
        }
    }


class MerchantCreate(MerchantBase):
    pass


class MerchantResponse(MerchantBase):
    id: UUID

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Kuro Ramen",
                "email": "contact@kuroramen.com",
                "phone": "+1-217-555-1234",
            }
        }
    }