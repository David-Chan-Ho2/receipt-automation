from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from config.db import get_db
from crud.merchant import (
    create_merchant,
    get_merchant,
    list_merchants,
    delete_merchant,
)
from schemas.merchant import MerchantCreate, MerchantResponse

router = APIRouter(prefix="/merchants", tags=["merchants"])


@router.post("/", response_model=MerchantResponse, status_code=status.HTTP_201_CREATED)
def create_merchant_route(
    merchant_in: MerchantCreate,
    db: Session = Depends(get_db),
):
    return create_merchant(db, merchant_in)


@router.get("/", response_model=list[MerchantResponse])
def list_merchants_route(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return list_merchants(db, skip=skip, limit=limit)


@router.get("/{merchant_id}", response_model=MerchantResponse)
def get_merchant_route(
    merchant_id: UUID,
    db: Session = Depends(get_db),
):
    merchant = get_merchant(db, merchant_id)
    if not merchant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Merchant not found",
        )
    return merchant


@router.delete("/{merchant_id}", response_model=MerchantResponse)
def delete_merchant_route(
    merchant_id: UUID,
    db: Session = Depends(get_db),
):
    merchant = delete_merchant(db, merchant_id)
    if not merchant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Merchant not found",
        )
    return merchant