import uuid
from decimal import Decimal
from datetime import datetime
from typing import Optional, List

from sqlalchemy import String, ForeignKey, Numeric, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


class Receipt(Base):
    __tablename__ = "receipts"

    merchant_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("merchants.id"),
        nullable=False,
        index=True,
    )

    address_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        ForeignKey("addresses.id"),
        nullable=True,
        index=True,
    )

    currency: Mapped[str] = mapped_column(String(3), nullable=False, default="USD")
    subtotal: Mapped[Optional[Decimal]] = mapped_column(Numeric(12, 2), nullable=True)
    tax: Mapped[Optional[Decimal]] = mapped_column(Numeric(12, 2), nullable=True)
    tip: Mapped[Optional[Decimal]] = mapped_column(Numeric(12, 2), nullable=True)
    total: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)

    raw_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    payment_method: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    purchased_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    merchant: Mapped["Merchant"] = relationship(
        back_populates="receipts",
    )

    address: Mapped[Optional["Address"]] = relationship(
        back_populates="receipts",
    )

    items: Mapped[List["LineItem"]] = relationship(
        back_populates="receipt",
        cascade="all, delete-orphan",
    )