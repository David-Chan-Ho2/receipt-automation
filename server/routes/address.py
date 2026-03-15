from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from config.db import get_db
from crud.address import (
    create_address,
    get_address,
    list_addresses_by_merchant,
    delete_address,
)
from schemas.address import AddressCreate, AddressResponse

router = APIRouter(prefix="/addresses", tags=["addresses"])


@router.post("/", response_model=AddressResponse, status_code=status.HTTP_201_CREATED)
def create_address_route(
    address_in: AddressCreate,
    db: Session = Depends(get_db),
):
    return create_address(db, address_in)


@router.get("/{address_id}", response_model=AddressResponse)
def get_address_route(
    address_id: UUID,
    db: Session = Depends(get_db),
):
    address = get_address(db, address_id)
    if not address:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Address not found",
        )
    return address


@router.get("/merchant/{merchant_id}", response_model=list[AddressResponse])
def list_addresses_by_merchant_route(
    merchant_id: UUID,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return list_addresses_by_merchant(db, merchant_id=merchant_id, skip=skip, limit=limit)


@router.delete("/{address_id}", response_model=AddressResponse)
def delete_address_route(
    address_id: UUID,
    db: Session = Depends(get_db),
):
    address = delete_address(db, address_id)
    if not address:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Address not found",
        )
    return address