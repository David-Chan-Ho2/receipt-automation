from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from config.db import get_db
from crud.receipt import (
    create_receipt,
    get_receipt,
    list_receipts,
    list_receipts_by_merchant,
    delete_receipt,
)
from schemas.receipt import ReceiptCreate, ReceiptResponse

router = APIRouter(prefix="/receipts", tags=["receipts"])


@router.post("/", response_model=ReceiptResponse, status_code=status.HTTP_201_CREATED)
def create_receipt_route(
    receipt_in: ReceiptCreate,
    db: Session = Depends(get_db),
):
    return create_receipt(db, receipt_in)


@router.get("/", response_model=list[ReceiptResponse])
def list_receipts_route(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return list_receipts(db, skip=skip, limit=limit)


@router.get("/{receipt_id}", response_model=ReceiptResponse)
def get_receipt_route(
    receipt_id: UUID,
    db: Session = Depends(get_db),
):
    receipt = get_receipt(db, receipt_id)
    if not receipt:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Receipt not found",
        )
    return receipt


@router.get("/merchant/{merchant_id}", response_model=list[ReceiptResponse])
def list_receipts_by_merchant_route(
    merchant_id: UUID,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return list_receipts_by_merchant(db, merchant_id=merchant_id, skip=skip, limit=limit)


@router.delete("/{receipt_id}", response_model=ReceiptResponse)
def delete_receipt_route(
    receipt_id: UUID,
    db: Session = Depends(get_db),
):
    receipt = delete_receipt(db, receipt_id)
    if not receipt:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Receipt not found",
        )
    return receipt