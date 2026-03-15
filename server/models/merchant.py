from typing import List, Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base

class Merchant(Base):
    __tablename__ = "merchants"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    phone: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)

    addresses: Mapped[List["Address"]] = relationship(
        back_populates="merchant",
        cascade="all, delete-orphan",
    )

    receipts: Mapped[List["Receipt"]] = relationship(
        back_populates="merchant",
    )