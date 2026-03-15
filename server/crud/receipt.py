from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from models.receipt import Receipt
from models.line_item import LineItem
from schemas.receipt import ReceiptCreate


def create_receipt(db: Session, receipt_in: ReceiptCreate) -> Receipt:
    receipt = Receipt(
        merchant_id=receipt_in.merchant_id,
        address_id=receipt_in.address_id,
        currency=receipt_in.currency,
        subtotal=receipt_in.subtotal,
        tax=receipt_in.tax,
        tip=receipt_in.tip,
        total=receipt_in.total,
        payment_method=receipt_in.payment_method,
        purchased_at=receipt_in.purchased_at,
    )

    for item_in in receipt_in.items:
        item = LineItem(
            name=item_in.name,
            description=item_in.description,
            quantity=item_in.quantity,
            unit_price=item_in.unit_price,
            amount=item_in.amount,
        )
        receipt.items.append(item)

    db.add(receipt)
    db.commit()
    db.refresh(receipt)
    return receipt


def get_receipt(db: Session, receipt_id: UUID) -> Receipt | None:
    stmt = (
        select(Receipt)
        .options(
            selectinload(Receipt.items),
            selectinload(Receipt.merchant),
            selectinload(Receipt.address),
        )
        .where(Receipt.id == receipt_id)
    )
    return db.scalar(stmt)


def list_receipts(db: Session, skip: int = 0, limit: int = 100) -> list[Receipt]:
    stmt = (
        select(Receipt)
        .options(
            selectinload(Receipt.items),
            selectinload(Receipt.merchant),
            selectinload(Receipt.address),
        )
        .offset(skip)
        .limit(limit)
    )
    return list(db.scalars(stmt).all())


def list_receipts_by_merchant(
    db: Session, merchant_id: UUID, skip: int = 0, limit: int = 100
) -> list[Receipt]:
    stmt = (
        select(Receipt)
        .options(
            selectinload(Receipt.items),
            selectinload(Receipt.merchant),
            selectinload(Receipt.address),
        )
        .where(Receipt.merchant_id == merchant_id)
        .offset(skip)
        .limit(limit)
    )
    return list(db.scalars(stmt).all())


def delete_receipt(db: Session, receipt_id: UUID) -> Receipt | None:
    receipt = get_receipt(db, receipt_id)
    if not receipt:
        return None

    db.delete(receipt)
    db.commit()
    return receipt