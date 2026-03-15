from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session

from models.merchant import Merchant
from schemas.merchant import MerchantCreate


def create_merchant(db: Session, merchant_in: MerchantCreate) -> Merchant:
    merchant = Merchant(
        name=merchant_in.name,
        email=merchant_in.email,
        phone=merchant_in.phone,
    )
    db.add(merchant)
    db.commit()
    db.refresh(merchant)
    return merchant


def get_merchant(db: Session, merchant_id: UUID) -> Merchant | None:
    stmt = select(Merchant).where(Merchant.id == merchant_id)
    return db.scalar(stmt)


def get_merchant_by_name(db: Session, name: str) -> Merchant | None:
    stmt = select(Merchant).where(Merchant.name == name)
    return db.scalar(stmt)


def list_merchants(db: Session, skip: int = 0, limit: int = 100) -> list[Merchant]:
    stmt = select(Merchant).offset(skip).limit(limit)
    return list(db.scalars(stmt).all())


def delete_merchant(db: Session, merchant_id: UUID) -> Merchant | None:
    merchant = get_merchant(db, merchant_id)
    if not merchant:
        return None

    db.delete(merchant)
    db.commit()
    return merchant