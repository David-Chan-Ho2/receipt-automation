from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session

from models.address import Address
from schemas.address import AddressCreate

def create_address(db: Session, address_in: AddressCreate) -> Address:
    address = Address(
        merchant_id=address_in.merchant_id,
        line1=address_in.line1,
        line2=address_in.line2,
        city=address_in.city,
        state=address_in.state,
        postal_code=address_in.postal_code,
        country=address_in.country,
    )
    db.add(address)
    db.commit()
    db.refresh(address)
    return address


def get_address(db: Session, address_id: UUID) -> Address | None:
    stmt = select(Address).where(Address.id == address_id)
    return db.scalar(stmt)


def list_addresses_by_merchant(
    db: Session, merchant_id: UUID, skip: int = 0, limit: int = 100
) -> list[Address]:
    stmt = (
        select(Address)
        .where(Address.merchant_id == merchant_id)
        .offset(skip)
        .limit(limit)
    )
    return list(db.scalars(stmt).all())


def delete_address(db: Session, address_id: UUID) -> Address | None:
    address = get_address(db, address_id)
    if not address:
        return None

    db.delete(address)
    db.commit()
    return address